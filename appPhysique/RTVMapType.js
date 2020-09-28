/**
 * Provides remote access to rendered RTV vector tiles.
 *
 * @file RTVMapType.js
 * @date 2017-08-07 12:40 PDT
 * @author Paul Reuter/Joseph Chen
 * @version 4.0.1
 *
 * @modifications
 * 1.0.0 - 2008-01-30 - Initially conceived, prototyped.
 * 2.0.0 - 2009-07-25 - Public API redesign
 * 2.0.1 - 2009-08-07 - Modifications: Changed some initialization inheritance
 * 2.0.2 - 2009-11-09 - Modify: Changed path on sandbar.
 * 2.0.3 - 2009-11-09 - Undo path change on sandbar (CeNCOOS legacy).
 * 2.0.4 - 2009-12-14 - Changed tile server, tile status server.
 * 2.0.4 - 2010-02-23 - BugFix: setHourly, setAveraged default values.
 * 2.0.4 - 2010-02-23 - Modified callback handler: dynamic func generation.
 * 2.0.4 - 2010-02-25 - BugFix: finAvail shouldn't set time if user did.
 * 2.0.5 - 2010-04-14 - Add: getStation/Network[Count] methods.
 * 2.0.6 - 2010-10-19 - Add: getLatestTimestampAtLatLng(latlng)
 * 3.0.0 - 2012-07-24 - Major revision for Google Maps v3 API.
 * 3.0.1 - 2012-11-29 - New object name, same methods, same intention.
 * 3.0.2 - 2013-08-23 - BugFix via John Maurer: getTileUrl dateline wrap.
 * 3.0.3 - 2014-01-06 - Modify: getTileUrl to support multiple countries.
 * 3.0.4 - 2014-09-12 - Modify: hfrnet became hfrnet-old for hardware upgrade
 * 3.0.5 - 2014-10-10 - Modify: hfrnet-old became hfrnet
 * 3.0.6 - 2015-01-29 - Add: getEarliestTimestamp
 * 3.0.7 - 2015-09-28 - BugFix: Google Maps changed something.
 * 3.0.8 - 2015-09-28 - BugFix: improve initialization.
 * 4.0.0 - 2017-06-02 - Added support for global
 * 4.0.1 - 2017-08-07 - Added support for https
 */



/**
 * opts: google.maps.ImageMapTypeOptions
 * alt, getTileUrl, maxZoom, minZoom, name, opacity, tielSize
 */
function RTVMapType(map,opts) {
  opts = opts || {};

  this.minZoom = opts.minZoom || 0;
  this.maxZoom = opts.maxZoom || 12;
  this.opacity = opts.opacity || 0.8;
  this.tileSize = opts.tileSize || new google.maps.Size(256,256);

  this.map = map;
  this.pfx = opts.pfx || 'a';
  this.tld = opts.tld || 'us';
  this.extension = opts.extension || 'png';
  this.res = opts.res || 6000;
  this.range = opts.range || [0,50];
  this.country = opts.country || 'us';

  this.ts = null;
  this.scheme = opts.scheme || 4;
  this.version = '4.0.0';
  this.self = this;

  google.maps.event.addListener(this,'statechange',this.refresh);
  google.maps.event.addListener(this,"network_loaded",this.m_synchronizedLoad);
  google.maps.event.addListener(this,"latest_loaded",this.m_synchronizedLoad);

  // Stuff for tracking most recent layers.
  this.m_upperTimestamps = [];
  this.m_networkStatus = null;
  this.m_initializeAvailability();
  this.m_initializeNetworkStatus();
}; // END: constructor RTVMapType
RTVMapType.prototype = new google.maps.MVCObject();


/**
 * getTileUrl is used by getTile, but is no longer required by interface.
 */
RTVMapType.prototype.getTileUrl = function(t,z) {
  if( z < this.minZoom || z > this.maxZoom || !this.ts ) {
    return '';
  }

  var d = new Date(this.ts*1000);
  var yyyy_mm = d.gmstrftime("%Y-%m");
  var yyyymmdd_hh00 = d.gmstrftime("%Y%m%d_%H00");
  var zz = (z<10) ? '0'+z : z;

  /**
   * BugFix Work-around:
   *
   * t.x exceeds allowed tile index in certain circumstances,
   * when date-line is present in the viewport.
   *
   * @author John Maurer
   * @since 2013-08-23
   */
  var nx = Math.pow(2,z);
  //return 'http://mosaic.ucsd.edu/tiles/rtv/'+this.tld +'/'+
  return '//mosaic.ucsd.edu/tiles/rtv/'+this.tld +'/'+
    this.pfx+'/'+this.res+'/'+yyyy_mm+'/'+yyyymmdd_hh00+
    '/'+zz+'/z'+z+'y'+t.y+'x'+((nx+t.x)%nx)+'.'+
    this.extension+'?rng='+this.range.join(',') +
    '&scheme='+this.scheme;
}; // END: function getTileUrl(t,z)



/**
 * Since Google Maps v3.22, we're forced to inherit from MVCObject
 * and provide getTile.
 * Since ImageMapType initializes from a non-mutable MapType,
 * we actually have to build the whole DOM element.
 * We had to reverse engineer ImageMapType's node to optimize performance.
 */
RTVMapType.prototype.getTile = function(coord, zoom, ownerDocument) {
  var url = this.getTileUrl(coord, zoom);
  var div = ownerDocument.createElement('div');
  div.innerHTML = '<img src="//maps.gstatic.com/mapfiles/transparent.png" draggable="false">';
  div.style['-moz-user-select'] = 'none';
  if( url ) {
    div.style.background = 'url('+url+')';
  }
  div.style.margin = '0';
  div.style.padding = '0';
  div.style.border = '0 none';
  div.style.opacity = this.opacity;
  div.style.width = this.tileSize.width + 'px';
  div.style.height = this.tileSize.height + 'px';
  return div;
};


RTVMapType.keys = function(arr) {
  var ks = [];
  for( var k in arr ) {
    ks.push(k);
  }
  return ks;
};

RTVMapType.values = function(arr) {
  var vs = [];
  for( var k in arr ) {
    vs.push(arr[k]);
  }
  return vs;
};

RTVMapType.array_map = function(keys,vals) {
  var amap = {};
  while( keys.length > 0 && vals.length > 0 ) {
    amap[keys.shift()] = vals.shift();
  }
  return amap;
};

RTVMapType.inArray = function(item,arr) {
  for(var k in arr) {
    if( arr[k] == item ) {
      return k;
    }
  }
  return -1;
};

RTVMapType.prototype.getStation = function(callsign,netname) {
  if( this.haveNetworkStatus() ) {
    var use_netname = (typeof(netname)!="undefined");
    var hdr = RTVMapType.keys( this.m_networkStatus.meta.keys.stations );
    var sta_ix = RTVMapType.inArray( 'sta', hdr );
    var net_ix = RTVMapType.inArray( 'net', hdr );
    if( sta_ix < 0 || net_ix < 0 ) {
      return false;
    }
    for(var i=0,n=this.m_networkStatus.data.stations.length; i<n; i++) {
      var obj = this.m_networkStatus.data.stations[i];
      if( obj[sta_ix] == callsign ) {
        if( use_netname ) {
          if( obj[net_ix] == netname ) {
            return RTVMapType.array_map(hdr,obj);
          }
        } else {
          return RTVMapType.array_map(hdr,obj);
        }
      }
    }
  }
  return false;
}; // END: function getStation(callsign,network?)


RTVMapType.prototype.getStations = function() {
  if( this.haveNetworkStatus() ) {
    var stas = [];
    var hdr = RTVMapType.keys( this.m_networkStatus.meta.keys.stations );
    var sta_ix = RTVMapType.inArray( 'sta', hdr );
    if( sta_ix < 0 ) {
      return false;
    }
    for(var i=0,n=this.m_networkStatus.data.stations.length; i<n; i++) {
      stas.push( this.m_networkStatus.data.stations[i][sta_ix] );
    }
    return stas;
  }
  return false;
}; // END: function getStations()


RTVMapType.prototype.getStationCount = function() {
  if( this.haveNetworkStatus() ) {
    return this.m_networkStatus.data.status.nSites;
  }
  return false;
}; // END: function getStationCount()


RTVMapType.prototype.getNetwork = function(netname) {
  if( this.haveNetworkStatus() ) {
    var hdr = RTVMapType.keys( this.m_networkStatus.meta.keys.stations );
    var net_ix = RTVMapType.inArray( 'net', hdr );
    if( net_ix < 0 ) {
      return false;
    }
    for(var i=0,n=this.m_networkStatus.data.networks.length; i<n; i++) {
      var obj = this.m_networkStatus.data.networks[i];
      if( obj[net_ix] == netname ) {
        return obj;
      }
    }
  }
  return false;
}; // END: function getNetwork(netname)


RTVMapType.prototype.getNetworks = function() {
  if( this.haveNetworkStatus() ) {
    var nets = [];
    var hdr = RTVMapType.keys( this.m_networkStatus.meta.keys.networks );
    var net_ix = RTVMapType.inArray( 'net', hdr );
    if( net_ix < 0 ) {
      return false;
    }
    for(var i=0,n=this.m_networkStatus.data.networks.length; i<n; i++) {
      nets.push( this.m_networkStatus.data.networks[i][net_ix] );
    }
    return nets;
  }
  return false;
}; // END: function getNetworks()


RTVMapType.prototype.getNetworkCount = function() {
  if( this.haveNetworkStatus() ) {
    return this.m_networkStatus.data.status.nNets;
  }
  return false;
}; // END: function getNetworkCount()


RTVMapType.prototype.getNetworkUpdateTime = function() {
  if( this.haveNetworkStatus() ) {
    return this.m_networkStatus.data.status.latest;
  }
  return false;
}; // END: function getNetworkUpdateTime()


RTVMapType.prototype.getLatestTimestamp = function() {
  var timerec = this.m_getSelectedTimestampRecord();
  if( !timerec ) {
    // not loaded yet, listen for RTVMapType 'load' event.
    return false;
  }
  return Number(timerec["latest"]);
};

RTVMapType.prototype.getEarliestTimestamp = function() {
  var timerec = this.m_getSelectedTimestampRecord();
  if( !timerec ) {
    // not loaded yet, listen for RTVMapType 'load' event.
    return false;
  }
  return Number(timerec["earliest"]);
};


RTVMapType.prototype.setLatestTimestamp = function() {
  var ts = this.getLatestTimestamp();
  return (ts===false) ? false : this.setTimestamp(ts);
};


RTVMapType.prototype.setLatestTimestampAtLatLng = function(latlng,cb) {
  var that = this;
  this.getLatestTimestampAtLatLng(latlng,function(ts,obj) {
    var ret = (ts>0) ? that.setTimestamp(ts) : false;
    // Call user function if present.
    if( typeof(cb) !== "undefined" ) {
      cb.call(that,ts,obj);
    }
    return ret;
  });
};


RTVMapType.prototype.getLatestTimestampAtLatLng = function(latlng,func) {
  if( !latlng || !latlng.constructor ) {
    return false;
  }

  var qstring = 'll='+latlng.toUrlValue() +
    '&res=' + this.getResolution() +
    '&pfx=' + this.getPrefix();

  // Generate unique function name and define it.
  var fname = '__ltll_'+this.pfx+'_'+this.res+'_'+this.ts+'_'+
              (new Date()).getTime();
  var fbody = ' google.maps.event.trigger(window,"e_'+fname+'",obj); '+
              ' google.maps.event.clearListeners(window,"e_'+fname+'"); ';
  window[fname] = new Function('obj', fbody);

  var head = document.getElementsByTagName("head")[0];
  var scriptTag = document.getElementById('dataScript_'+fname);
  if(scriptTag) head.removeChild(scriptTag);
  script = document.createElement('script');
  //script.src = 'http://hfrnet.ucsd.edu/rtv/ll.php?'+qstring+'&callback='+fname;
  script.src = '//hfrnet.ucsd.edu/rtv/ll.php?'+qstring+'&callback='+fname;
  script.type = 'text/javascript';
  script.id = 'dataScript_'+fname;
  head.appendChild(script);

  // Listen for event triggered from unique function.
  var that = this;
  google.maps.event.addListener(window,'e_'+fname,function(obj) {
    // Call user function.
    if( obj.error ) {
      func.call(that,-1,obj);
    } else {
      func.call(that,Number(obj.latest),obj);
    }
  });
  return true;
};


RTVMapType.prototype.getVectorData = function(latlng,func) {
  if( !latlng || !latlng.constructor ) {
    return false;
  }

  var qstring = 'lat='+latlng.lat()+'&lon='+latlng.lng()+
    '&time='+this.getTimestamp()+'&res='+this.getResolution()+
    '&pfx='+this.getPrefix();

  // Generate unique function name and define it.
  var fname = '__vdata_'+this.pfx+'_'+this.res+'_'+this.ts+'_'+
              (new Date()).getTime();
  var fbody = ' google.maps.event.trigger(window,"e_'+fname+'",obj); '+
              ' google.maps.event.clearListeners(window,"e_'+fname+'"); ';
  window[fname] = new Function('obj', fbody);

  var head = document.getElementsByTagName("head")[0];
  var scriptTag = document.getElementById('dataScript_'+fname);
  if(scriptTag) head.removeChild(scriptTag);
  // hfrnet for US, mosaic for global
  var server;
  var page; // country code
  if( this.tld == 'us' ) {
    server="hfrnet.ucsd.edu";
    page="";
  }
  else {
    server="mosaic.ucsd.edu";
    page="p="+this.tld+"&";
  }
  script = document.createElement('script');
  script.src = '//'+server+'/rtv/nn.php?'+page+qstring+'&callback='+fname;
  script.type = 'text/javascript';
  script.id = 'dataScript_'+fname;
  head.appendChild(script);

  // Listen for event triggered from unique function.
  var that = this;
  google.maps.event.addListener(window,'e_'+fname,function(obj) {
    // Call user function.
    func.call(that,obj);
  });
  return true;
};


RTVMapType.prototype.m_initializeNetworkStatus = function() {
  // Generate unique function name and define it.
  var fname = '__rtv_'+(new Date()).getTime();
  var fbody = ' google.maps.event.trigger(window,"e_'+fname+'",obj); '+
              ' google.maps.event.clearListeners(window,"e_'+fname+'"); ';
  window[fname] = new Function('obj', fbody);

  var head = document.getElementsByTagName("head")[0];
  var scriptTag = document.getElementById('networkScript_'+fname);
  if(scriptTag) head.removeChild(scriptTag);
  script = document.createElement('script');
  //script.src = 'http://hfrnet.ucsd.edu/rtv/sm.php?callback='+fname;
  script.src = '//hfrnet.ucsd.edu/rtv/sm.php?callback='+fname;
  script.type = 'text/javascript';
  script.id = 'networkScript_'+fname;
  head.appendChild(script);

  var that = this;
  google.maps.event.addListener(window,'e_'+fname,function(obj) {
    // Call user function.
    that.m_networkStatus = obj;
    google.maps.event.trigger(that,"network_loaded");
  });
  return true;
};

RTVMapType.prototype.m_initializeAvailability = function() {
  // Generate unique function name and define it.
  var fname = '__rtv_'+this.pfx+'_'+this.res+'_'+this.ts+'_'+
              (new Date()).getTime();
  var fbody = ' google.maps.event.trigger(window,"e_'+fname+'",obj); '+
              ' google.maps.event.clearListeners(window,"e_'+fname+'"); ';
  window[fname] = new Function('obj', fbody);

  var head = document.getElementsByTagName("head")[0];
  var scriptTag = document.getElementById('loadScript_'+fname);
  if(scriptTag) head.removeChild(scriptTag);
  script = document.createElement('script');
  //script.src = 'http://hfrnet.ucsd.edu/rtv/ts.php?callback='+fname;
  script.src = '//hfrnet.ucsd.edu/rtv/ts.php?callback='+fname;
  script.type = 'text/javascript';
  script.id = 'loadScript_'+fname;
  head.appendChild(script);

  google.maps.event.bind(window,'e_'+fname,this,this.m_finalizeAvailability);
};


RTVMapType.prototype.m_finalizeAvailability = function(obj) {
  this.m_upperTimestamps = obj;
  var timerec = this.m_getSelectedTimestampRecord();
  if( !timerec ) {
    alert("Invalid configuration.  The service may be down.");
    return false;
  }
  // It's possible that the user changed the time before this returned.
  // So only set timestamp if it hasn't been initialized.
  if( this.ts == null || this.ts == 0 ) {
    this.setTimestamp(Number(timerec["latest"]));
  }
  google.maps.event.trigger(this,'latest_loaded',Number(timerec["latest"]));
};


RTVMapType.prototype.haveTimestamps = function() {
  return (this.m_upperTimestamps.length>0) ? true : false;
}

RTVMapType.prototype.haveNetworkStatus = function() {
  return (this.m_networkStatus) ? true : false;
}

RTVMapType.prototype.m_synchronizedLoad = function() {
  if( this.haveTimestamps() && this.haveNetworkStatus() ) {
    google.maps.event.trigger(this,'load',this.getTimestamp());
  }
};


RTVMapType.prototype.m_getSelectedTimestampRecord = function() {
  for(var i=0,n=this.m_upperTimestamps.length; i<n; i++) {
    if( this.m_upperTimestamps[i].resolution == this.res
    &&  this.m_upperTimestamps[i].prefix == this.pfx ) {
      return this.m_upperTimestamps[i];
    }
  }
  return null;
};


RTVMapType.prototype.setExtension = function(ext) {
  if( this.extension != ext ) {
    this.extension = ext;
    google.maps.event.trigger(this,'statechange');
  }
};
RTVMapType.prototype.getExtension = function() {
  return this.extension;
};


RTVMapType.prototype.setOpacity = function(op) {
  op = (op>1) ? op/100 : op;
  if( this.opacity != op ) {
    this.opacity = (op>1) ? op/100 : op;
    google.maps.event.trigger(this,'statechange');
  }
};
// GMap2 interface
RTVMapType.prototype.getOpacity = function() {
  return this.opacity;
};


RTVMapType.prototype.setMinZoom = function(zoom) {
  if( this.minZoom != zoom ) {
    this.minZoom = zoom;
    google.maps.event.trigger(this,'statechange');
  }
};
RTVMapType.prototype.getMinZoom = function() {
  return this.minZoom;
};


RTVMapType.prototype.setMaxZoom = function(zoom) {
  if( this.maxZoom != zoom ) {
    this.mazZoom = zoom;
    google.maps.event.trigger(this,'statechange');
  }
};
RTVMapType.prototype.getMaxZoom = function() {
  return this.mazZoom;
};


RTVMapType.prototype.setZoomRange = function(z0,z1) {
  if( this.minZoom != z0 || this.maxZoom != z1 ) {
    this.minZoom = z0;
    this.mazZoom = z1;
    google.maps.event.trigger(this,'statechange');
  }
};


// GMap2 interface
RTVMapType.prototype.minResolution = function() {
  return this.minZoom;
}


// GMap2 interface
RTVMapType.prototype.maxResolution = function() {
  return this.maxZoom;
}


// GMap2 interface
RTVMapType.prototype.getCopyright = function(gllb,zoom) {
  if( !this.copyrights ) {
    return 'CORDC';
  }
  return this.copyrights.getCopyrightNotice(gllb,zoom);
};


// GMap2 interface
RTVMapType.prototype.isPng = function() {
  return (String(this.extension).toLowerCase()=="png");
};



RTVMapType.prototype.setColorRange = function(lo,hi) {
  if( this.range[0] != lo || this.range[1] != hi ) {
    this.range = [lo,hi];
    google.maps.event.trigger(this,'statechange');
  }
};
RTVMapType.prototype.getColorRange = function() {
  return this.range;
};


RTVMapType.prototype.setColorScheme = function(scheme) {
  if( this.scheme != scheme ) {
    this.scheme = scheme;
    google.maps.event.trigger(this,'statechange');
  }
};
RTVMapType.prototype.getColorScheme = function() {
  return this.scheme;
};

RTVMapType.prototype.getColorbarUrl = function(w,h) {
  w = w || 220;
  h = h || 45;

  var px = 8;
  var py = 15;

  h = Math.max(5,h-2*py);
  w = Math.max(30,w-2*px);

  return '//cordc.ucsd.edu/projects/mapping/maps/img/php/cb.php'+
  '?range='+this.range.join(',')+'&scheme='+this.scheme+
  '&width='+w+'&height='+h+'&padding='+py+','+px+
  '&title='+escape('Current Strength (cm/s)')+
  '&font_size=10&ticks=6';
};

RTVMapType.prototype.setPrefix = function(pfx) {
  if( this.pfx != pfx ) {
    this.pfx = pfx;
    google.maps.event.trigger(this,'statechange');
  }
};
RTVMapType.prototype.getPrefix = function() {
  return this.pfx;
};


RTVMapType.prototype.setResolution = function(res) {
  res = this.getResolutionMeters(res);
  if( this.res != res ) {
    this.res = res;
    google.maps.event.trigger(this,'statechange');
  }
};
RTVMapType.prototype.getResolution = function() {
  return this.res;
};
RTVMapType.prototype.getResolutionMeters = function(res) {
  if( String(parseInt(res)) == String(res) ) {
    return Number(res);
  }
  var pts = String(res).match(/^\s*(\d+)([^0-9]+)\s*$/);
  if( pts[2].toLowerCase() == 'km' ) {
    return Number(pts[1])*1000;
  }
  return Number(pts[1]);
};

RTVMapType.prototype.setAveraged = function(bAvg) {
  var pfx = (typeof(bAvg)=='undefined' || bAvg) ? "a" : "h";
  return this.setPrefix( pfx );
};

RTVMapType.prototype.setHourly = function(bHour) {
  var pfx = (typeof(bHour)=='undefined' || bHour) ? "h" : "a";
  return this.setPrefix( pfx );
};

RTVMapType.prototype.setTimestamp = function(ts) {
  // If timestamp isn't specified, use yesterday as as start.
  // The starting point is later initialized as the most recent available
  // upon startup.  This just provides extra fall-back.
  if( typeof(ts) == "undefined" ) {
    // default to -1 day
    var d = new Date();
    ts = Math.floor(d.getTime()/1000) - 86400;
    ts -= ts%3600;
  }
  if( this.ts != ts && ts !== 0) {
    this.ts = ts;
    // console.log('timechange: '+ts);
    google.maps.event.trigger(this,'timechange',ts);
    google.maps.event.trigger(this,'statechange');
  }
};
RTVMapType.prototype.getTimestamp = function() {
  return this.ts;
};

RTVMapType.prototype.getVersion = function() {
  return this.version;
};

RTVMapType.prototype.refresh = function() {
  for(var i=0,n=this.map.overlayMapTypes.getLength(); i<n; i++) {
    if( this.map.overlayMapTypes.getAt(i) == this ) {
      obj = this.map.overlayMapTypes.removeAt(i);
      this.map.overlayMapTypes.insertAt(i,obj);
      break;
    }
  }
}; // END: function refresh()


/**
 * Extra dependencies.
 */
/* other support functions -- thanks, ecmanaut! */
var strftime_funks = {
  zeropad: function( n ){ return n>9 ? n : '0'+n; },
  a: function(t) { return ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'][t.getDay()] },
  A: function(t) { return ['Sunday','Monday','Tuedsay','Wednesday','Thursday','Friday','Saturday'][t.getDay()] },
  b: function(t) { return ['Jan','Feb','Mar','Apr','May','Jun', 'Jul','Aug','Sep','Oct','Nov','Dec'][t.getMonth()] },
  B: function(t) { return ['January','February','March','April','May','June', 'July','August',
      'September','October','November','December'][t.getMonth()] },
  c: function(t) { return t.toString() },
  d: function(t) { return this.zeropad(t.getDate()) },
  H: function(t) { return this.zeropad(t.getHours()) },
  I: function(t) { return this.zeropad((t.getHours() + 12) % 12) },
  m: function(t) { return this.zeropad(t.getMonth()+1) }, // month-1
  M: function(t) { return this.zeropad(t.getMinutes()) },
  p: function(t) { return this.H(t) < 12 ? 'AM' : 'PM'; },
  S: function(t) { return this.zeropad(t.getSeconds()) },
  w: function(t) { return t.getDay() }, // 0..6 == sun..sat
  y: function(t) { return this.zeropad(this.Y(t) % 100); },
  Y: function(t) { return t.getFullYear(); },
  Z: function(t) {
    tzo = t.getTimezoneOffset();
    pfx = (tzo>0) ? "-" : "+";
    return pfx+this.zeropad(Math.floor(tzo/60))+this.zeropad(t.getTimezoneOffset()%60);
  },
  '%': function(t) { return '%' }
};



var gmstrftime_funks = {
  zeropad: function( n ){ return n>9 ? n : '0'+n; },
  a: function(t) { return ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'][t.getUTCDay()] },
  A: function(t) { return ['Sunday','Monday','Tuedsay','Wednesday','Thursday','Friday','Saturday'][t.getUTCDay()] },
  b: function(t) { return ['Jan','Feb','Mar','Apr','May','Jun', 'Jul','Aug','Sep','Oct','Nov','Dec'][t.getUTCMonth()] },
  B: function(t) { return ['January','February','March','April','May','June', 'July','August',
      'September','October','November','December'][t.getUTCMonth()] },
  c: function(t) { return t.toGMTString() },
  d: function(t) { return this.zeropad(t.getUTCDate()) },
  H: function(t) { return this.zeropad(t.getUTCHours()) },
  I: function(t) { return this.zeropad((t.getUTCHours() + 12) % 12) },
  m: function(t) { return this.zeropad(t.getUTCMonth()+1) }, // month-1
  M: function(t) { return this.zeropad(t.getUTCMinutes()) },
  p: function(t) { return this.H(t) < 12 ? 'AM' : 'PM'; },
  S: function(t) { return this.zeropad(t.getSeconds()) },
  w: function(t) { return t.getUTCDay() }, // 0..6 == sun..sat
  y: function(t) { return this.zeropad(this.Y(t) % 100); },
  Y: function(t) { return t.getUTCFullYear() },
  Z: function(t) { return "UTC" },
  '%': function(t) { return '%' }
};


Date.prototype.strftime = function (fmt) {
    var t = this;
    for (var s in strftime_funks) {
        if (s.length == 1 )
            fmt = fmt.replace('%' + s, strftime_funks[s](t));
    }
    return fmt;
};

Date.prototype.gmstrftime = function (fmt) {
  var t = this;
  for (var s in gmstrftime_funks) {
    if (s.length == 1 )
      fmt = fmt.replace('%' + s, gmstrftime_funks[s](t));
  }
  return fmt;
};

if ( typeof(TrimPath) != "undefined" ) {
    TrimPath.parseTemplate_etc.modifierDef.strftime = function (t, fmt) {
        return new Date(t).strftime(fmt);
    }
}
if ( typeof(TrimPath) != "undefined" ) {
    TrimPath.parseTemplate_etc.modifierDef.gmstrftime = function (t, fmt) {
        return new Date(t).gmstrftime(fmt);
    }
}
(function(){var aa="function"==typeof Object.create?Object.create:function(a){var b=function(){};b.prototype=a;return new b},ba;if("function"==typeof Object.setPrototypeOf)ba=Object.setPrototypeOf;else{var ca;a:{var da={P:!0},ea={};try{ea.__proto__=da;ca=ea.P;break a}catch(a){}ca=!1}ba=ca?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var fa=ba,ha=function(a,b){a.prototype=aa(b.prototype);a.prototype.constructor=a;if(fa)fa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.C=b.prototype},f=this,h=function(a){return void 0!==a},l=function(a){return"string"==typeof a},m=function(a){return"boolean"==typeof a},p=function(a){return"number"==typeof a},ia=function(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";else if("function"==b&&"undefined"==typeof a.call)return"object";return b},q=function(a){var b=typeof a;return"object"==b&&null!=a||"function"==b},ka=function(a,b,c){return a.call.apply(a.bind,arguments)},la=function(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}},r=function(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?r=ka:r=la;return r.apply(null,arguments)},ma=Date.now||function(){return+new Date},t=function(a,b){a=a.split(".");var c=f;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)!a.length&&h(b)?c[d]=b:c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}},u=function(a,b){function c(){}c.prototype=b.prototype;a.C=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.T=function(a,c,g){for(var d=Array(arguments.length-2),e=2;e<arguments.length;e++)d[e-2]=arguments[e];return b.prototype[c].apply(a,d)}};var na=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if(l(a))return l(b)&&1==b.length?a.indexOf(b,0):-1;for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},oa=Array.prototype.forEach?function(a,b){Array.prototype.forEach.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=l(a)?a.split(""):a,e=0;e<c;e++)e in d&&b.call(void 0,d[e],e,a)};var pa=function(){};var qa=function(a){qa[" "](a);return a};qa[" "]=function(){};var v=function(){var a=document.body.offsetHeight;this.width=document.body.offsetWidth;this.height=a};v.prototype.aspectRatio=function(){return this.width/this.height};v.prototype.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};v.prototype.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};v.prototype.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};var x=function(a){return(new ra).m(a)},ra=function(){};ra.prototype.m=function(a){var b=[];sa(this,a,b);return b.join("")};var sa=function(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if("array"==ia(b)){var d=b;b=d.length;c.push("[");for(var e="",g=0;g<b;g++)c.push(e),sa(a,d[g],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(g=b[d],"function"!=typeof g&&(c.push(e),ta(d,c),c.push(":"),sa(a,g,c),e=","));c.push("}");return}}switch(typeof b){case "string":ta(b,c);break;case "number":c.push(isFinite(b)&&!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}},ua={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},va=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g,ta=function(a,b){b.push('"',a.replace(va,function(a){var b=ua[a];b||(b="\\u"+(a.charCodeAt(0)|65536).toString(16).substr(1),ua[a]=b);return b}),'"')};var y=function(a,b,c,d){this.j=a;this.g=b;this.a=c;this.f=d},z=function(a){return new y(a.j,a.g,a.a,a.f)};y.prototype.ceil=function(){this.j=Math.ceil(this.j);this.g=Math.ceil(this.g);this.a=Math.ceil(this.a);this.f=Math.ceil(this.f);return this};y.prototype.floor=function(){this.j=Math.floor(this.j);this.g=Math.floor(this.g);this.a=Math.floor(this.a);this.f=Math.floor(this.f);return this};y.prototype.round=function(){this.j=Math.round(this.j);this.g=Math.round(this.g);this.a=Math.round(this.a);this.f=Math.round(this.f);return this};var A=!1,C=function(a){if(a=a.match(/[\d]+/g))a.length=3};(function(){if(navigator.plugins&&navigator.plugins.length){var a=navigator.plugins["Shockwave Flash"];if(a&&(A=!0,a.description)){C(a.description);return}if(navigator.plugins["Shockwave Flash 2.0"]){A=!0;return}}if(navigator.mimeTypes&&navigator.mimeTypes.length&&(a=navigator.mimeTypes["application/x-shockwave-flash"],A=!(!a||!a.enabledPlugin))){C(a.enabledPlugin.description);return}if("undefined"!=typeof ActiveXObject){try{var b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7");A=!0;C(b.GetVariable("$version"));return}catch(c){}try{b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6");A=!0;return}catch(c){}try{b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash"),A=!0,C(b.GetVariable("$version"))}catch(c){}}})();var ya=function(a,b){if(a)for(var c in a)Object.prototype.hasOwnProperty.call(a,c)&&b.call(void 0,a[c],c,a)};var za=function(a,b,c){c=void 0===c?{}:c;this.error=a;this.context=b.context;this.line=b.line||-1;this.msg=b.message||"";this.file=b.file||"";this.id=b.id||"jserror";this.meta=c};var D=function(a,b,c){a.addEventListener&&a.addEventListener(b,c,!1)};var Aa=/^https?:\/\/(\w|-)+\.cdn\.ampproject\.(net|org)(\?|\/|$)/,Ba=function(a,b){this.a=a;this.f=b},Ca=function(a,b){this.url=a;this.I=!!b;this.depth=p(void 0)?void 0:null};var Da=function(a){var b=!1,c=!1;c=void 0===c?!1:c;b=void 0===b?!1:b;f.google_image_requests||(f.google_image_requests=[]);var d=f.document.createElement("img");if(b){var e=function(){if(b){var a=f.google_image_requests,c=na(a,d);0<=c&&Array.prototype.splice.call(a,c,1)}d.removeEventListener&&d.removeEventListener("load",e,!1);d.removeEventListener&&d.removeEventListener("error",e,!1)};D(d,"load",e);D(d,"error",e)}c&&(d.referrerPolicy="no-referrer");d.src=a;f.google_image_requests.push(d)};var Ea=function(){this.g="&";this.j=h(void 0)?void 0:"trn";this.o=!1;this.f={};this.u=0;this.a=[]},Fa=function(a,b){var c={};c[a]=b;return[c]},Ha=function(a,b,c,d,e){var g=[];ya(a,function(a,k){(a=Ga(a,b,c,d,e))&&g.push(k+"="+a)});return g.join(b)},Ga=function(a,b,c,d,e){if(null==a)return"";b=b||"&";c=c||",$";"string"==typeof c&&(c=c.split(""));if(a instanceof Array){if(d=d||0,d<c.length){for(var g=[],n=0;n<a.length;n++)g.push(Ga(a[n],b,c,d+1,e));return g.join(c[d])}}else if("object"==typeof a)return e=e||0,2>e?encodeURIComponent(Ha(a,b,c,d,e+1)):"...";return encodeURIComponent(String(a))},E=function(a,b,c,d){a.a.push(b);a.f[b]=Fa(c,d)},Ja=function(a){var b="https://pagead2.googlesyndication.com/pagead/gen_204?id=jserror&",c=Ia(a)-27;if(0>c)return"";a.a.sort(function(a,b){return a-b});for(var d=null,e="",g=0;g<a.a.length;g++)for(var n=a.a[g],k=a.f[n],B=0;B<k.length;B++){if(!c){d=null==d?n:d;break}var w=Ha(k[B],a.g,",$");if(w){w=e+w;if(c>=w.length){c-=w.length;b+=w;e=a.g;break}else a.o&&(e=c,w[e-1]==a.g&&--e,b+=w.substr(0,e),e=a.g,c=0);d=null==d?n:d}}g="";a.j&&null!=d&&(g=e+a.j+"="+d);return b+g+""},Ia=function(a){if(!a.j)return 4E3;var b=1,c;for(c in a.f)b=c.length>b?c.length:b;return 4E3-a.j.length-b-a.g.length-1};var Ka=function(a){if(.01>Math.random())try{if(a instanceof Ea)var b=a;else b=new Ea,ya(a,function(a,c){var d=b,e=d.u++;a=Fa(c,a);d.a.push(e);d.f[e]=a});var c=Ja(b);c&&Da(c)}catch(d){}};var La=function(){var a=void 0===a?f:a;return(a=a.performance)&&a.now?a.now():null};var Ma=function(a){var b=a.toString();a.name&&-1==b.indexOf(a.name)&&(b+=": "+a.name);a.message&&-1==b.indexOf(a.message)&&(b+=": "+a.message);if(a.stack){a=a.stack;var c=b;try{-1==a.indexOf(c)&&(a=c+"\n"+a);for(var d;a!=d;)d=a,a=a.replace(/((https?:\/..*\/)[^\/:]*:\d+(?:.|\n)*)\2/,"$1");b=a.replace(/\n */g,"\n")}catch(e){b=c}}return b},Na=function(a,b,c){za.call(this,Error(a),{message:a,file:void 0===b?"":b,line:void 0===c?-1:c})};ha(Na,za);var Oa=function(a,b){this.a=a;this.f=b||Math.floor(2147483648*Math.random()).toString(36)+Math.abs(Math.floor(2147483648*Math.random())^ma()).toString(36)},Pa=function(a){var b={};oa(a,function(a){b[a.a]=a.f});return b},Qa=function(){var a=F.goog_safeframe_hlt,b=[];a&&ya(a,function(a,d){b.push(new Oa(parseInt(d,10),a))});return b};var G=function(a,b,c,d,e,g){this.o=a;this.status=1;this.g=b;this.u=c;this.H=d;this.F=!!e;this.j=Math.random();this.a={};this.f=null;this.D=r(this.G,this);this.A=g};ha(G,pa);G.prototype.G=function(a){if(a.origin===this.u&&(this.F||a.source==this.g)){var b=null;try{b=JSON.parse(a.data)}catch(c){}if(q(b)&&(a=b.i,b.c===this.o&&a!=this.j)){if(2!==this.status)try{this.status=2,Ra(this),this.f&&(this.f(),this.f=null)}catch(c){}a=b.s;b=b.p;if(l(a)&&(l(b)||q(b))&&this.a.hasOwnProperty(a))this.a[a](b)}}};var Ra=function(a){var b={};b.c=a.o;b.i=a.j;a.A&&(b.e=a.A);a.g.postMessage(x(b),a.u)};G.prototype.B=function(){if(1===this.status){try{this.g.postMessage&&Ra(this)}catch(a){}window.setTimeout(r(this.B,this),50)}};G.prototype.connect=function(a){a&&(this.f=a);D(window,"message",this.D);this.H&&this.B()};var Sa=function(a,b,c){var d={};d.c=a.o;d.i=a.j;d.s=b;d.p=c;try{a.g.postMessage(x(d),a.u)}catch(e){}};var Ta=function(a,b,c,d,e,g,n){this.g=z(a);this.f=z(b);this.a=n?z(n):null;this.A=c;this.j=z(d);this.o=e;this.u=g};Ta.prototype.m=function(){var a={windowCoords_t:this.g.j,windowCoords_r:this.g.g,windowCoords_b:this.g.a,windowCoords_l:this.g.f,frameCoords_t:this.f.j,frameCoords_r:this.f.g,frameCoords_b:this.f.a,frameCoords_l:this.f.f,styleZIndex:this.A,allowedExpansion_t:this.j.j,allowedExpansion_r:this.j.g,allowedExpansion_b:this.j.a,allowedExpansion_l:this.j.f,xInView:this.o,yInView:this.u};this.a&&(a.posCoords_t=this.a.j,a.posCoords_b=this.a.a,a.posCoords_l=this.a.f,a.posCoords_r=this.a.g);return x(a)};var H=function(a){a=JSON.parse(a);if(!(q(a)&&p(a.windowCoords_t)&&p(a.windowCoords_r)&&p(a.windowCoords_b)&&p(a.windowCoords_l)&&p(a.frameCoords_t)&&p(a.frameCoords_r)&&p(a.frameCoords_b)&&p(a.frameCoords_l)&&l(a.styleZIndex)&&p(a.allowedExpansion_t)&&p(a.allowedExpansion_r)&&p(a.allowedExpansion_b)&&p(a.allowedExpansion_l)&&p(a.xInView)&&0<=a.xInView&&1>=a.xInView&&p(a.yInView)&&0<=a.yInView&&1>=a.yInView)||h(a.posCoords_t)&&!p(a.posCoords_t)||h(a.posCoords_b)&&!p(a.posCoords_b)||h(a.posCoords_r)&&!p(a.posCoords_r)||h(a.posCoords_l)&&!p(a.posCoords_l)||h(a.posCoords_t)&&!(h(a.posCoords_b)&&h(a.posCoords_l)&&h(a.posCoords_r)))throw Error("Cannot parse JSON geometry");var b=new y(a.windowCoords_t,a.windowCoords_r,a.windowCoords_b,a.windowCoords_l),c=new y(a.frameCoords_t,a.frameCoords_r,a.frameCoords_b,a.frameCoords_l),d=new y(a.allowedExpansion_t,a.allowedExpansion_r,a.allowedExpansion_b,a.allowedExpansion_l),e;h(a.posCoords_t)&&(e=new y(a.posCoords_t,a.posCoords_r,a.posCoords_b,a.posCoords_l));return new Ta(b,c,a.styleZIndex,d,a.xInView,a.yInView,e)};var Ua=function(a){this.f=a;this.o=null;this.a=this.status=0;this.j=null;this.N="sfchannel"+a},I=function(a){return 1==a.status||2==a.status};var Va=function(){this.a=N};Va.prototype.m=function(){return x(this.a)};var Wa=function(){var a=O.expandByPush,b=O.readCookie,c=O.writeCookie;this.a=O.expandByOverlay;this.f=a;this.g=b;this.j=c};Wa.prototype.m=function(){return x({expandByOverlay:this.a,expandByPush:this.f,readCookie:this.g,writeCookie:this.j})};var ab=function(){var a=F.uid,b=F.hostPeerName,c=Xa,d=Ya,e=Za,g=F.reportCreativeGeometry,n=F.isDifferentSourceWindow,k=$a,B=F.sentinel,w=F.inFakeDecryptionExperiment;k=void 0===k?[]:k;this.A=a;this.f=b;this.g=c;this.u=d;this.j=e;this.B=g;this.o=n;this.D=k;this.a=void 0===B?"":B;this.F=void 0===w?!1:w};ab.prototype.m=function(){var a={};a=(a.uid=this.A,a.hostPeerName=this.f,a.initialGeometry=this.g.m(),a.permissions=this.u.m(),a.metadata=this.j.m(),a.reportCreativeGeometry=this.B,a.isDifferentSourceWindow=this.o,a.goog_safeframe_hlt=Pa(this.D),a.inFakeDecryptionExperiment=this.F,a);this.a&&(a.sentinel=this.a);return x(a)};var bb=/^([^;]+);(\d+);([\s\S]*)$/;var P=function(a,b){this.a=a;this.g=b};P.prototype.m=function(a){this.g&&(a.sentinel=this.g);return x(a)};var cb=function(a,b,c){P.call(this,a,void 0===c?"":c);this.version=b};u(cb,P);cb.prototype.m=function(){return cb.C.m.call(this,{uid:this.a,version:this.version})};var db=function(a,b,c,d){P.call(this,a,void 0===d?"":d);this.j=b;this.f=c};u(db,P);db.prototype.m=function(){return db.C.m.call(this,{uid:this.a,initialWidth:this.j,initialHeight:this.f})};var eb=function(a,b,c){P.call(this,a,void 0===c?"":c);this.f=b};u(eb,P);eb.prototype.m=function(){return eb.C.m.call(this,{uid:this.a,description:this.f})};var Q=function(a,b,c,d){P.call(this,a,void 0===d?"":d);this.f=b;this.push=c};u(Q,P);Q.prototype.m=function(){return Q.C.m.call(this,{uid:this.a,expand_t:this.f.j,expand_r:this.f.g,expand_b:this.f.a,expand_l:this.f.f,push:this.push})};var fb=function(a,b){P.call(this,a,void 0===b?"":b)};u(fb,P);fb.prototype.m=function(){return fb.C.m.call(this,{uid:this.a})};var gb=function(a,b,c){P.call(this,a,void 0===c?"":c);this.f=b};u(gb,P);gb.prototype.m=function(){return gb.C.m.call(this,{uid:this.a,shrink_t:this.f.j,shrink_r:this.f.g,shrink_b:this.f.a,shrink_l:this.f.f})};var hb=function(a,b,c,d){P.call(this,a,void 0===d?"":d);this.f=b;this.push=c};u(hb,P);hb.prototype.m=function(){return hb.C.m.call(this,{uid:this.a,resize_t:this.f.j,resize_r:this.f.g,resize_b:this.f.a,resize_l:this.f.f,push:this.push})};var R=function(a,b,c){P.call(this,a,void 0===c?"":c);this.j=b};u(R,P);var ib=function(a){a=JSON.parse(a);if(!(q(a)&&p(a.uid)&&l(a.newGeometry)))throw Error("Cannot parse JSON message");var b=H(a.newGeometry);return new R(a.uid,b,a.sentinel)};R.prototype.m=function(){var a={uid:this.a,newGeometry:this.j.m()};return R.C.m.call(this,a)};var jb=function(a,b,c,d,e,g){R.call(this,a,c,void 0===g?"":g);this.o=b;this.f=d;this.push=e};u(jb,R);jb.prototype.m=function(){var a={uid:this.a,success:this.o,newGeometry:this.j.m(),expand_t:this.f.j,expand_r:this.f.g,expand_b:this.f.a,expand_l:this.f.f,push:this.push};this.g&&(a.sentinel=this.g);return x(a)};var kb=function(a,b,c,d){R.call(this,a,c,void 0===d?"":d);this.f=b};u(kb,R);kb.prototype.m=function(){var a={uid:this.a,success:this.f,newGeometry:this.j.m()};this.g&&(a.sentinel=this.g);return x(a)};var lb=function(a,b,c,d,e){R.call(this,a,c,void 0===e?"":e);this.f=b;this.o=d};u(lb,R);lb.prototype.m=function(){var a={uid:this.a,success:this.f,newGeometry:this.j.m(),expand_t:this.o.j,expand_r:this.o.g,expand_b:this.o.a,expand_l:this.o.f};this.g&&(a.sentinel=this.g);return x(a)};var mb=function(a,b,c,d){P.call(this,a,void 0===d?"":d);this.width=b;this.height=c};u(mb,P);mb.prototype.m=function(){return mb.C.m.call(this,{uid:this.a,width:this.width,height:this.height})};var T=function(a){Ua.call(this,a.A);this.B=a.u;this.M=a.j;this.D=null;this.A=[];this.u=0;this.o=a.g;this.g=a.a;this.j=new G(this.N,window.parent,a.f,!0,a.o,this.g);var b=r(this.K,this);this.j.a.expand_response=b;b=r(this.G,this);this.j.a.collapse_response=b;b=r(this.F,this);this.j.a.resize_response=b;b=r(this.F,this);this.j.a.shrink_response=b;b=r(this.L,this);this.j.a.geometry_update=b;this.j.connect(r(this.O,this));this.status=1;S(this,"init_done",new cb(this.f,"1-0-31",this.g));a.B&&(a=r(T.prototype.J,this),D(window,"load",a),D(window,"resize",a))};ha(T,Ua);T.prototype.register=function(a,b,c){this.status=2;this.D=c;S(this,"register_done",new db(this.f,a,b,this.g))};var U=function(a,b){S(a,"report_error",new eb(a.f,b,a.g))};T.prototype.O=function(){for(var a=0;a<this.A.length;a++)Sa(this.j,this.A[a].type,this.A[a].message.m())};T.prototype.K=function(a){try{if(2!=this.status)throw Error("Container is not registered");if(3!=this.a)throw Error("Container is not expanding");if(!l(a))throw Error("Could not parse serialized message");var b=JSON.parse(a);if(!(q(b)&&p(b.uid)&&m(b.success)&&l(b.newGeometry)&&p(b.expand_t)&&p(b.expand_r)&&p(b.expand_b)&&p(b.expand_l)&&m(b.push)))throw Error("Cannot parse JSON message");var c=H(b.newGeometry);var d=new jb(b.uid,b.success,c,new y(b.expand_t,b.expand_r,b.expand_b,b.expand_l),b.push,b.sentinel);if(this.f!=d.a)throw Error("Wrong source container");this.a=d.o?2:0;this.o=d.j;V(this,d.o?"expanded":"failed",d.push?"exp-push":"exp-ovr","",{t:d.f.j,r:d.f.g,b:d.f.a,l:d.f.f,push:d.push})}catch(e){}};T.prototype.F=function(a){try{if(2!=this.status)throw Error("Container is not registered");if(5!=this.a)throw Error("Container is not resizing");if(!l(a))throw Error("Could not parse serialized message");try{var b=JSON.parse(a);if(!(q(b)&&p(b.uid)&&m(b.success)&&l(b.newGeometry)))throw Error("Cannot parse JSON message");var c=H(b.newGeometry);var d=new kb(b.uid,b.success,c,b.sentinel)}catch(n){var e=JSON.parse(a);if(!(q(e)&&p(e.uid)&&m(e.success)&&l(e.newGeometry)&&p(e.expand_t)&&p(e.expand_r)&&p(e.expand_b)&&p(e.expand_l)))throw Error("Cannot parse JSON message");var g=H(e.newGeometry);d=new lb(e.uid,e.success,g,new y(e.expand_t,e.expand_r,e.expand_b,e.expand_l),e.sentinel)}if(this.f!=d.a)throw Error("Wrong source container");this.a=d.f?4:0;this.o=d.j;V(this,d.f?"resized":"failed","resize","",{})}catch(n){}};T.prototype.G=function(a){try{if(2!=this.status)throw Error("Container is not registered");if(1!=this.a)throw Error("Container is not collapsing");if(!l(a))throw Error("Could not parse serialized message");var b=ib(a);if(this.f!=b.a)throw Error("Wrong source container");this.a=0;this.o=b.j;V(this,"collapsed","collapse","",void 0)}catch(c){}};T.prototype.L=function(a){try{if(!I(this))throw Error("Container is not initialized or registered");if(!l(a))throw Error("Could not parse serialized message");var b=ib(a);if(this.f!=b.a)throw Error("Wrong source container");this.o=b.j;V(this,"geom-update","","",void 0)}catch(c){}};var V=function(a,b,c,d,e){if(null!==a.D)try{a.D(b,{cmd:c,reason:d,info:e})}catch(g){U(a,"Could not manage to call user-supplied callback")}},nb=function(a,b,c,d){setTimeout(r(function(){V(this,a,b,c,d)},X),0)},S=function(a,b,c){2===a.j.status?Sa(a.j,b,c.m()):a.A.push({type:b,message:c})},ob=function(a){var b=new v;S(a,"creative_geometry_update",new mb(a.f,b.width,b.height,a.g))};T.prototype.H=function(){2==this.u&&ob(this);this.u=0};T.prototype.J=function(){switch(this.u){case 0:ob(this);setTimeout(r(this.H,this),200);this.u=1;break;case 1:this.u=2}};var Y=function(a,b,c){var d=window;return function(){var e=La();try{var g=b.apply(this,arguments)}catch(k){if(c)return c(a,k),g;throw k;}if(d.google_measure_js_timing&&e){e={label:a.toString(),value:e,duration:(La()||0)-e,type:3};var n=d.google_js_reporting_queue=d.google_js_reporting_queue||[];1024>n.length&&n.push(e)}return g}};var pb=function(a,b,c){if(2==X.status)U(X,"Called register multiple times");else if(!p(a)||0>=a)U(X,"Invalid initial width");else if(!p(b)||0>=b)U(X,"Invalid initial height");else{var d=null;if(null!=c){if("function"!=ia(c)){U(X,"Invalid callback function");return}d=c}X.register(a,b,d)}},qb=function(){return I(X)?{"exp-ovr":X.B.a,"exp-push":X.B.f,"read-cookie":X.B.g,"write-cookie":X.B.j}:(U(X,"Called supports on bad container"),null)},rb=function(){if(!I(X))return U(X,"Called geom on bad container"),null;var a=X.o,b={win:{t:a.g.j,r:a.g.g,b:a.g.a,l:a.g.f,w:a.g.g-a.g.f,h:a.g.a-a.g.j},self:{t:a.f.j,r:a.f.g,b:a.f.a,l:a.f.f,w:a.f.g-a.f.f,h:a.f.a-a.f.j,z:parseInt(a.A,10),xiv:a.o,yiv:a.u,iv:a.o*a.u},exp:{t:a.j.j,r:a.j.g,b:a.j.a,l:a.j.f,xs:!1,yx:!1}};a.a&&(b.pos={t:a.a.j,r:a.a.g,b:a.a.a,l:a.a.f,w:a.a.g-a.a.f,h:a.a.a-a.a.j});return b},sb=function(){if(!I(X))return U(X,"Called inViewPercentage on bad container"),null;var a=X.o;return a.o*a.u*100},tb=function(){if(!I(X))return U(X,"Called status on bad container"),null;switch(X.a){case 0:return"collapsed";case 1:return"collapsing";case 2:return"expanded";case 3:return"expanding";case 4:return"resized";case 5:return"resizing";default:return null}},ub=function(a,b){if(!I(X))return U(X,"Called meta on bad container"),null;if(!l(a)||/^[\s\xa0]*$/.test(null==a?"":String(a)))return U(X,"Invalid property name"),null;var c="shared";if(null!=b){if(!l(b)||/^[\s\xa0]*$/.test(null==b?"":String(b)))return U(X,"Invalid owner key"),null;c=b}b=X.M;return null!=b.a[c]&&null!=b.a[c][a]?b.a[c][a]:null},vb=function(a,b){2==X.status?!l(a)||/^[\s\xa0]*$/.test(a)?U(X,"Invalid cookie name"):((a=null==b)||!(a=q(b)&&l(b.info))||(a=null==b.expires)||(a=b.expires,a=q(a)&&"function"==typeof a.getFullYear),a?(nb("unsupported",null!=b?"write-cookie":"read-cookie","$sf.ext.cookie is not supported",b),U(X,"Used unsupported cookie operations")):(nb("failed","write-cookie","Invalid $sf.ext.cookie arguments",b),U(X,"Invalid cookie data"))):U(X,"Called cookie on unregistered container")},wb=function(a){if(2==X.status)if(0==X.a)if(q(a)&&(null!=a.t||null!=a.r||null!=a.b||null!=a.l)&&(null==a.t||p(a.t)&&0<=a.t)&&(null==a.r||p(a.r)&&0<=a.r)&&(null==a.b||p(a.b)&&0<=a.b)&&(null==a.l||p(a.l)&&0<=a.l)&&(null==a.push||m(a.push))){var b=new y(a.t||0,a.r||0,a.b||0,a.l||0);a=a.push||!1;var c=X;c.a=3;S(c,"expand_request",new Q(c.f,b,a,c.g))}else nb("failed",q(a)&&m(a.push)&&1==a.push?"exp-push":"exp-ovr","Invalid $sf.ext.expand arguments",a),U(X,"Invalid expand data");else U(X,"Called expand on uncollapsed container");else U(X,"Called expand on unregistered container")},xb=function(a){if(2==X.status)if(1==X.a||3==X.a||5==X.a)U(X,"Called resize on container in incorrect state.");else{var b=!q(a)||null==a.t&&null==a.r&&null==a.b&&null==a.l||null!=a.t&&!p(a.t)||null!=a.r&&!p(a.r)||null!=a.b&&!p(a.b)||null!=a.l&&!p(a.l)?null:a;if(b){a=new y(b.t||0,b.r||0,b.b||0,b.l||0);b=b.push||!1;var c=X;0<a.j||0<a.a||0<a.g||0<a.f?(c.a=3,S(c,"expand_request",new Q(c.f,a,b,c.g))):(c.a=5,S(c,"shrink_request",new gb(c.f,new y(-a.j,-a.g,-a.a,-a.f),c.g)));S(c,"resize_request",new hb(c.f,a,b,c.g))}else nb("failed","resize","Invalid $sf.ext.resize arguments",a),U(X,"Invalid resize data")}else U(X,"Called resize on unregistered container")},yb=function(){if(2==X.status){var a;(a=2==X.a)||(a=4==X.a);a?(a=X,a.a=1,S(a,"collapse_request",new fb(a.f,a.g))):U(X,"Called collapse on collapsed container")}else U(X,"Called collapse on unregistered container")},zb=function(){var a=function(a,c){var b=c;try{var e=new Ea;e.o=!0;E(e,1,"context",a);if(!(b.error&&b.meta&&b.id)){var g=b;b=new Na(Ma(g),g.fileName,g.lineNumber)}b.msg&&E(e,2,"msg",b.msg.substring(0,512));b.file&&E(e,3,"file",b.file);0<b.line&&E(e,4,"line",b.line);var n=[b.meta||{}];e.a.push(5);e.f[5]=n;g=f;b=[];n=null;do{var k=g;try{var B;if(B=!!k&&null!=k.location.href)b:{try{qa(k.foo);B=!0;break b}catch(ja){}B=!1}var w=B}catch(ja){w=!1}if(w){var K=k.location.href;n=k.document&&k.document.referrer||null}else K=n,n=null;b.push(new Ca(K||""));try{g=k.parent}catch(ja){g=null}}while(g&&k!=g);K=0;for(var L=b.length-1;K<=L;++K)b[K].depth=L-K;k=f;if(k.location&&k.location.ancestorOrigins&&k.location.ancestorOrigins.length==b.length-1)for(L=1;L<b.length;++L){var M=b[L];M.url||(M.url=k.location.ancestorOrigins[L-1]||"",M.I=!0)}var wa=new Ca(f.location.href,!1);k=null;var xa=b.length-1;for(M=xa;0<=M;--M){var J=b[M];!k&&Aa.test(J.url)&&(k=J);if(J.url&&!J.I){wa=J;break}}J=null;var Kb=b.length&&b[xa].url;0!=wa.depth&&Kb&&(J=b[xa]);var W=new Ba(wa,J);W.f&&E(e,6,"top",W.f.url||"");E(e,7,"url",W.a.url||"");Ka(e)}catch(ja){try{Ka({context:"ecmserr",rctx:a,msg:Ma(ja),url:W&&W.a.url})}catch(Ob){}}throw c;};t("$sf.ext.register",Y(441,pb,a));t("$sf.ext.supports",Y(443,qb,a));t("$sf.ext.geom",Y(438,rb,a));t("$sf.ext.inViewPercentage",Y(439,sb,a));t("$sf.ext.status",Y(442,tb,a));t("$sf.ext.meta",Y(440,ub,a));t("$sf.ext.cookie",Y(436,vb,a));t("$sf.ext.expand",Y(437,wb,a));t("$sf.ext.collapse",Y(435,yb,a))},Ab=null,Bb=!1;try{Bb=!!f.sf_.cfg._context.ampcontextVersion}catch(a){}var Cb=window,Db=!(Cb!=Cb.parent&&Cb.parent==Cb.top);try{var Eb,Fb;if(f.sf_)Eb=f.sf_.cfg,Fb=f.sf_.v;else{var Gb,Hb=bb.exec(window.name);if(null===Hb)throw Error("Cannot parse serialized data");var Ib=+Hb[2],Jb=Hb[3];if(Ib>Jb.length)throw Error("Cannot parse serialized data");Gb={S:Hb[1],content:Jb.substr(0,Ib),R:Jb.substr(Ib)};Eb=JSON.parse(Gb.R);Fb=Gb.S}var Lb=Fb,Mb,F=Eb;if(!(p(F.uid)&&l(F.hostPeerName)&&l(F.initialGeometry)&&l(F.permissions)&&l(F.metadata)&&m(F.reportCreativeGeometry)&&m(F.isDifferentSourceWindow))||null!=F.sentinel&&!l(F.sentinel)||null!=F.inFakeDecryptionExperiment&&!m(F.inFakeDecryptionExperiment)||F.goog_safeframe_hlt&&!q(F.goog_safeframe_hlt))throw Error("Cannot parse config");var Xa=H(F.initialGeometry),O=JSON.parse(F.permissions);if(!(q(O)&&m(O.expandByOverlay)&&m(O.expandByPush)&&m(O.readCookie)&&m(O.writeCookie)))throw Error("Cannot parse JSON permissions");var Ya=new Wa,Z=JSON.parse(F.metadata),Nb;(Nb=!q(Z))||(Nb=!(q(Z.shared)&&l(Z.shared.sf_ver)&&p(Z.shared.ck_on)&&l(Z.shared.flash_ver)&&(!Z.shared.canonical_url||l(Z.shared.canonical_url))&&(!Z.shared.amp||q(Z.shared.amp)&&(!Z.shared.amp.canonical_url||l(Z.shared.amp.canonical_url)))));if(Nb)throw Error("Cannot parse JSON metadata");var N={shared:{sf_ver:Z.shared.sf_ver,ck_on:Z.shared.ck_on,flash_ver:Z.shared.flash_ver}};Z.shared.canonical_url&&(N.shared.canonical_url=Z.shared.canonical_url);Z.shared.amp&&(N.shared.is_amp=!0,N.shared.canonical_url=Z.shared.amp.canonical_url);var Za=new Va,$a=Qa();Mb=new ab;if(!Mb.a&&"1-0-31"!=Lb)throw Error("Host has different version from ext container");Ab=new T(Mb);if(Bb||!Db)zb(),Ab.g&&t("$sf.ext.resize",xb)}catch(a){}f.sf_=void 0;window.name="";var X=Ab;}).call(this);

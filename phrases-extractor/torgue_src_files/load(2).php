var isCompatible=function(){if(navigator.appVersion.indexOf('MSIE')!==-1&&parseFloat(navigator.appVersion.split('MSIE')[1])<6){return false;}return true;};var startUp=function(){mw.config=new mw.Map(true);mw.loader.addSource({"local":{"loadScript":"/load.php","apiScript":"/api.php"},"common":{"loadScript":"https://slot1-images.wikia.nocookie.net/__load/-/","apiScript":"/api.php"}});mw.loader.register([["site",1520594100,[],"site"],["noscript",1202225400,[],"noscript"],["startup",1549259100,[],"startup"],["user",1202225400,[],"user"],["user.groups",1202225400,[],"user"],["user.options",1549259100,[],"private"],["user.cssprefs",1549259100,["mediawiki.user"],"private"],["user.tokens",1202225400,[],"private"],["filepage",1202225400],["mediawiki.language.data",1542134700,["mediawiki.language.init"]],["skins.monobook",1548854100,[],null,"common"],["jquery",1548854100,[],null,"common"],["jquery.appear",1548854100,[],null,"common"],["jquery.arrowSteps",1548854100,[],null,"common"],[
"jquery.async",1548854100,[],null,"common"],["jquery.autoEllipsis",1548854100,["jquery.highlightText"],null,"common"],["jquery.byteLength",1548854100,[],null,"common"],["jquery.byteLimit",1548854100,["jquery.byteLength"],null,"common"],["jquery.checkboxShiftClick",1548854100,[],null,"common"],["jquery.client",1548854100,[],null,"common"],["jquery.collapsibleTabs",1548854100,[],null,"common"],["jquery.color",1548854100,["jquery.colorUtil"],null,"common"],["jquery.colorUtil",1548854100,[],null,"common"],["jquery.cookie",1548854100,[],null,"common"],["jquery.delayedBind",1548854100,[],null,"common"],["jquery.expandableField",1548854100,["jquery.delayedBind"],null,"common"],["jquery.farbtastic",1548854100,["jquery.colorUtil"],null,"common"],["jquery.footHovzer",1548854100,[],null,"common"],["jquery.form",1548854100,[],null,"common"],["jquery.getAttrs",1548854100,[],null,"common"],["jquery.highlightText",1548854100,[],null,"common"],["jquery.hoverIntent",1548854100,[],null,"common"],[
"jquery.json",1548854100,[],null,"common"],["jquery.localize",1548854100,[],null,"common"],["jquery.makeCollapsible",1548854100,[],null,"common"],["jquery.messageBox",1548854100,[],null,"common"],["jquery.mockjax",1548854100,[],null,"common"],["jquery.mw-jump",1548854100,[],null,"common"],["jquery.mwExtension",1548854100,[],null,"common"],["jquery.placeholder",1548854100,[],null,"common"],["jquery.qunit",1548854100,[],null,"common"],["jquery.qunit.completenessTest",1548854100,["jquery.qunit"],null,"common"],["jquery.spinner",1548854100,[],null,"common"],["jquery.suggestions",1548854100,["jquery.autoEllipsis"],null,"common"],["jquery.tabIndex",1548854100,[],null,"common"],["jquery.tablesorter",1548854100,["jquery.mwExtension"],null,"common"],["jquery.textSelection",1548854100,[],null,"common"],["jquery.validate",1548854100,[],null,"common"],["jquery.xmldom",1548854100,[],null,"common"],["jquery.tipsy",1548854100,[],null,"common"],["jquery.ui.core",1548854100,["jquery"],"jquery.ui",
"common"],["jquery.ui.widget",1548854100,[],"jquery.ui","common"],["jquery.ui.mouse",1548854100,["jquery.ui.widget"],"jquery.ui","common"],["jquery.ui.position",1548854100,[],"jquery.ui","common"],["jquery.ui.draggable",1548854100,["jquery.ui.core","jquery.ui.mouse","jquery.ui.widget"],"jquery.ui","common"],["jquery.ui.droppable",1548854100,["jquery.ui.core","jquery.ui.mouse","jquery.ui.widget","jquery.ui.draggable"],"jquery.ui","common"],["jquery.ui.resizable",1548854100,["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse"],"jquery.ui","common"],["jquery.ui.selectable",1548854100,["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse"],"jquery.ui","common"],["jquery.ui.sortable",1548854100,["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse"],"jquery.ui","common"],["jquery.ui.accordion",1548854100,["jquery.ui.core","jquery.ui.widget"],"jquery.ui","common"],["jquery.ui.autocomplete",1548854100,["jquery.ui.core","jquery.ui.widget","jquery.ui.position"],"jquery.ui","common"],[
"jquery.ui.button",1548854100,["jquery.ui.core","jquery.ui.widget"],"jquery.ui","common"],["jquery.ui.datepicker",1548854100,["jquery.ui.core"],"jquery.ui","common"],["jquery.ui.dialog",1548854100,["jquery.ui.core","jquery.ui.widget","jquery.ui.button","jquery.ui.draggable","jquery.ui.mouse","jquery.ui.position","jquery.ui.resizable"],"jquery.ui","common"],["jquery.ui.progressbar",1548854100,["jquery.ui.core","jquery.ui.widget"],"jquery.ui","common"],["jquery.ui.slider",1548854100,["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse"],"jquery.ui","common"],["jquery.ui.tabs",1548854100,["jquery.ui.core","jquery.ui.widget"],"jquery.ui","common"],["jquery.effects.core",1548854100,["jquery"],"jquery.ui","common"],["jquery.effects.blind",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.bounce",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.clip",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.drop",1548854100,[
"jquery.effects.core"],"jquery.ui","common"],["jquery.effects.explode",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.fade",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.fold",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.highlight",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.pulsate",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.scale",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.shake",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.slide",1548854100,["jquery.effects.core"],"jquery.ui","common"],["jquery.effects.transfer",1548854100,["jquery.effects.core"],"jquery.ui","common"],["mediawiki",1548854100,[],null,"common"],["mediawiki.api",1548854100,["mediawiki.util"],null,"common"],["mediawiki.api.category",1548854100,["mediawiki.api","mediawiki.Title"],null,"common"],["mediawiki.api.edit",
1548854100,["mediawiki.api","mediawiki.Title"],null,"common"],["mediawiki.api.parse",1548854100,["mediawiki.api"],null,"common"],["mediawiki.api.titleblacklist",1548854100,["mediawiki.api","mediawiki.Title"],null,"common"],["mediawiki.api.watch",1548854100,["mediawiki.api","mediawiki.user"],null,"common"],["mediawiki.debug",1548854100,["jquery.footHovzer"],null,"common"],["mediawiki.debug.init",1548854100,["mediawiki.debug"],null,"common"],["mediawiki.feedback",1548854100,["mediawiki.api.edit","mediawiki.Title","mediawiki.jqueryMsg","jquery.ui.dialog"],null,"common"],["mediawiki.htmlform",1548854100,[],null,"common"],["mediawiki.Title",1548854100,["jquery.byteLength","mediawiki.util"],null,"common"],["mediawiki.Uri",1548854100,[],null,"common"],["mediawiki.user",1548854100,["jquery.cookie"],null,"common"],["mediawiki.util",1548854100,["jquery.client","jquery.cookie","jquery.messageBox","jquery.mwExtension"],null,"common"],["mediawiki.action.edit",1548854100,["jquery.textSelection",
"jquery.byteLimit"],null,"common"],["mediawiki.action.history",1548854100,["jquery.ui.button"],"mediawiki.action.history","common"],["mediawiki.action.history.diff",1548854100,[],"mediawiki.action.history","common",["sass"]],["mediawiki.action.view.dblClickEdit",1548854100,["mediawiki.util","mediawiki.page.startup"],null,"common"],["mediawiki.action.view.metadata",1548854100,[],null,"common"],["mediawiki.action.view.rightClickEdit",1548854100,[],null,"common"],["mediawiki.action.watch.ajax",1548854100,["mediawiki.api.watch","mediawiki.util"],null,"common"],["mediawiki.language",1548854100,["mediawiki.language.data","mediawiki.cldr"],null,"common"],["mediawiki.cldr",1548854100,["mediawiki.libs.pluralruleparser"],null,"common"],["mediawiki.libs.pluralruleparser",1548854100,[],null,"common"],["mediawiki.language.init",1548854100,[],null,"common"],["mediawiki.jqueryMsg",1548854100,["mediawiki.util","mediawiki.language"],null,"common"],["mediawiki.language.months",1548854100,[
"mediawiki.language"],null,"common"],["mediawiki.language.names",1536598800,["mediawiki.language.init"]],["mediawiki.libs.jpegmeta",1548854100,[],null,"common"],["mediawiki.page.ready",1548854100,["jquery.checkboxShiftClick","jquery.makeCollapsible","jquery.mw-jump","mediawiki.util"],null,"common"],["mediawiki.page.startup",1548854100,["jquery.client","mediawiki.util"],null,"common"],["mediawiki.special",1548854100,[],null,"common"],["mediawiki.special.block",1548854100,["mediawiki.util"],null,"common"],["mediawiki.special.changeemail",1548854100,["mediawiki.util"],null,"common"],["mediawiki.special.changeslist",1548854100,["jquery.makeCollapsible"],null,"common"],["mediawiki.special.movePage",1548854100,["jquery.byteLimit"],null,"common"],["mediawiki.special.preferences",1548854100,[],null,"common"],["mediawiki.special.recentchanges",1548854100,["mediawiki.special"],null,"common"],["mediawiki.special.search",1548854100,[],null,"common"],["mediawiki.special.undelete",1548854100,[],null
,"common"],["mediawiki.special.upload",1548854100,["mediawiki.libs.jpegmeta","mediawiki.util"],null,"common"],["mediawiki.special.javaScriptTest",1548854100,["jquery.qunit"],null,"common"],["test.sinonjs",1548854100,[],null,"common"],["mediawiki.tests.qunit.testrunner",1549259100,["jquery.qunit","jquery.qunit.completenessTest","mediawiki.page.startup","mediawiki.page.ready","test.sinonjs"],null,"common"],["mediawiki.legacy.ajax",1548854100,["mediawiki.util","mediawiki.legacy.wikibits"],null,"common"],["mediawiki.legacy.commonPrint",1548854100,[],null,"common"],["mediawiki.legacy.config",1548854100,["mediawiki.legacy.wikibits"],null,"common"],["mediawiki.legacy.IEFixes",1548854100,["mediawiki.legacy.wikibits"],null,"common"],["mediawiki.legacy.mwsuggest",1548854100,["mediawiki.legacy.wikibits"],null,"common"],["mediawiki.legacy.preview",1548854100,["mediawiki.legacy.wikibits"],null,"common"],["mediawiki.legacy.protect",1548854100,["mediawiki.legacy.wikibits","jquery.byteLimit"],null,
"common"],["mediawiki.legacy.shared",1548854100,[],null,"common"],["mediawiki.legacy.upload",1548854100,["jquery.spinner","mediawiki.util"],null,"common"],["mediawiki.legacy.wikibits",1548854100,["mediawiki.util","wikia.importScript"],null,"common"],["mediawiki.legacy.wikiprintable",1548854100,[],null,"common"],["amd",1548854100,[],null,"common"],["amd.shared",1202225400,["wikia.instantGlobals","wikia.cache","wikia.cookies","wikia.document","wikia.geo","wikia.fbLocale","wikia.loader","wikia.location","wikia.log","wikia.mw","wikia.nirvana","wikia.querystring","wikia.history","wikia.throbber","wikia.thumbnailer","wikia.tracker","wikia.window","wikia.abTest","underscore"],null,"common"],["wikia.window",1548854100,["amd"],null,"common"],["wikia.cache",1548854100,["amd","wikia.window"],null,"common"],["wikia.document",1548854100,["amd","wikia.window"],null,"common"],["wikia.location",1548854100,["amd","wikia.window"],null,"common"],["wikia.nirvana",1548854100,["amd"],null,"common"],[
"wikia.mw",1548854100,["amd","wikia.window"],null,"common"],["wikia.fbLocale",1548854100,["wikia.geo"],null,"common"],["wikia.loader",1548854100,["amd","wikia.window","wikia.mw","wikia.nirvana","wikia.fbLocale"],null,"common"],["wikia.querystring",1548854100,["amd","wikia.window"],null,"common"],["wikia.history",1548854100,["amd","wikia.window"],null,"common"],["wikia.cookies",1548854100,["amd","wikia.window"],null,"common"],["wikia.log",1548854100,["amd","wikia.querystring","wikia.cookies"],null,"common"],["wikia.abTest",1548854100,["amd","wikia.window"],null,"common"],["wikia.instantGlobals",1548854100,["amd","wikia.window"],null,"common"],["wikia.thumbnailer",1548854100,["amd"],null,"common"],["wikia.geo",1548854100,["amd","wikia.cookies","wikia.querystring"],null,"common"],["wikia.tracker",1548854100,["amd","wikia.window","wikia.log","wikia.tracker.stub"],null,"common"],["wikia.tracker.stub",1548854100,["amd","wikia.window"],null,"common"],["wikia.throbber",1548854100,["amd"],null,
"common"],["underscore",1548854100,["amd"],null,"common"],["wikia.aim",1548854100,["amd"],null,"common"],["wikia.uniqueId",1548854100,["amd"],null,"common"],["wikia.modernizr",1549259100,["amd","modernizr"],null,"common"],["wikia.mustache",1548854100,["amd"],null,"common"],["wikia.underscore",1548854100,["amd","wikia.window"],null,"common"],["wikia.stickyElement",1548854100,["amd","wikia.window","wikia.document","wikia.underscore"],null,"common"],["wikia.jquery.ui",1548854100,["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse","jquery.ui.position","jquery.ui.draggable","jquery.ui.droppable","jquery.ui.sortable","jquery.ui.autocomplete","jquery.ui.slider","jquery.ui.tabs","jquery.ui.datepicker"],"jquery.ui","common"],["jquery.mustache",1548854100,["wikia.mustache"],null,"common"],["jquery.autocomplete",1548854100,[],null,"common"],["jquery.dataTables",1548854100,[],null,"common"],["jquery.timeago",1548854100,[],null,"common"],["wikia.yui",1548854100,[],"yui","common"],[
"wikia.importScript",1548854100,[],null,"common"],["wikia.article.edit",1548854100,["wikia.tracker"],null,"common"],["jquery.uls.data",1548854100],["jquery.i18n",1548854100,["mediawiki.libs.pluralruleparser"]],["ext.math.mathjax",1548854100,[],"ext.math.mathjax"],["ext.math.mathjax.enabler",1548854100],["ext.wikia.TimeAgoMessaging",1548854100,["jquery.timeago","mediawiki.jqueryMsg"]],["ext.designSystem",1202225400],["wikia.ext.instantGlobals",1549259100,[],null,"common"],["wikia.ext.instantGlobalsOverride",1548854100,[],null,"common"],["ext.bannerNotifications",1202225400],["ext.quickTools",1548854100,["mediawiki.user","mediawiki.util"]],["ext.createUserPage",1548854100,["mediawiki.user","mediawiki.util"]],["ext.quickAdopt",1548854100,["mediawiki.util","ext.createUserPage"]],["ext.wikia.authPreferences",1548854100],["ext.wikia.facebookTags",1548854100,[],null,"common"],["ext.wikia.multiLookup",1548854100],["ext.wikia.ListGlobalUsers",1548854100],["ext.geshi.local",1202225400],[
"ext.siteWideMessages.anon",1548854100],["ext.scribunto",1548854100],["ext.scribunto.edit",1548854100,["ext.scribunto","mediawiki.api"]],["ext.wikia.InfoboxBuilder",1548854100,[],null,"local",["sass"]],["ext.categoryTree",1548854100],["ext.categoryTree.css",1548854100],["ext.checkUser",1548854100,["mediawiki.util"]],["ext.cite",1548854100,["jquery.tooltip"]],["jquery.tooltip",1548854100],["ext.wikia.ajaxpoll",1548854100,[],null,"local",["sass"]],["ext.wikia.WMU",1548854100,["wikia.yui","jquery.aim"]],["ext.wikia.LinkSuggest",1548854100,["jquery.ui.autocomplete"]],["ext.wikia.ListUsers",1548854100,["jquery.ui.autocomplete","jquery.dataTables"],null,"local",["sass"]],["ext.abuseFilter",1548854100],["ext.abuseFilter.edit",1548854100,["jquery.textSelection","jquery.spinner"]],["ext.abuseFilter.tools",1548854100,["jquery.spinner"]],["ext.abuseFilter.examine",1548854100],["ext.tabber",1548854100],["ext.nuke",1548854100],["ext.userLogin",1202225400],["ext.UserProfilePage.Lightbox",1548854100,
["mediawiki.jqueryMsg"],null,"local",["sass"]],["ext.renameuser.modal",1548854100,["mediawiki.util"]],["ext.Chat2.ChatBanModal",1548854100],["ext.Chat2.ChatWidget",1202225400],["ext.Chat2.ChatBanList",1548854100,["jquery.dataTables","wikia.nirvana"],null,"local",["sass"]],["ext.Chat2",1202225400,["mediawiki.jqueryMsg"]],["ext.AdminDashboard",1202225400],["wikia.ext.abtesting",1546300800,[],null,"common"],["wikia.ext.abt3sting",1546300800,[],null,"common"],["wikia.ext.abtest",1548854100],["wikia.ext.abtesting.edit.styles",1548854100,[],null,"local",["sass"]],["wikia.ext.abtesting.edit",1548854100],["oojs",1548854100],["oojs-ui",1548854100,["oojs","oojs-ui.styles"]],["oojs-ui.styles",1548854100],["jquery.visibleText",1548854100],["Base64.js",1548854100],["easy-deflate.core",1548854100,["Base64.js"]],["easy-deflate.deflate",1548854100,["easy-deflate.core"]],["unicodejs",1548854100],["unicodejs.wordbreak",1202225400,["unicodejs"]],["papaparse",1548854100],["rangefix",1548854100],[
"ext.visualEditor.viewPageTarget.init",1548854100,["jquery.client","mediawiki.page.startup","mediawiki.Title","mediawiki.Uri","mediawiki.util","user.options","ext.visualEditor.track"]],["ext.visualEditor.viewPageTarget.noscript",1548854100],["ext.visualEditor.viewPageTarget",1548854100,["ext.visualEditor.base","ext.visualEditor.mediawiki","ext.visualEditor.core.desktop","jquery.placeholder","mediawiki.feedback","mediawiki.jqueryMsg","mediawiki.util"]],["ext.visualEditor.mobileViewTarget",1548854100,["ext.visualEditor.base","ext.visualEditor.mediawiki.mobile","ext.visualEditor.core.mobile","ext.visualEditor.mwimage.core"]],["ext.visualEditor.ve",1548854100],["ext.visualEditor.track",1548854100,["ext.visualEditor.ve"]],["ext.visualEditor.base",1548854100,["oojs","oojs-ui","unicodejs","rangefix","ext.visualEditor.ve"]],["ext.visualEditor.mediawiki",1548854100,["jquery.visibleText","jquery.byteLength","jquery.client","mediawiki.api","mediawiki.language","mediawiki.Title","mediawiki.Uri",
"mediawiki.user","mediawiki.util","easy-deflate.deflate","user.options","user.tokens","ext.visualEditor.base","ext.visualEditor.track"]],["ext.visualEditor.mediawiki.mobile",1548854100,["ext.visualEditor.mediawiki","ext.visualEditor.core.mobile"]],["ext.visualEditor.standalone",1548854100,["ext.visualEditor.base","jquery.i18n"]],["ext.visualEditor.data",1548854100,["ext.visualEditor.base"]],["ext.visualEditor.core",1548854100,["unicodejs","papaparse","jquery.uls.data","ext.visualEditor.base"]],["ext.visualEditor.core.desktop",1548854100,["ext.visualEditor.core"]],["ext.visualEditor.core.mobile",1548854100,["ext.visualEditor.core"]],["ext.visualEditor.mwcore",1548854100,["ext.visualEditor.core","mediawiki.Title","mediawiki.action.history.diff","mediawiki.user","mediawiki.util","mediawiki.jqueryMsg","jquery.autoEllipsis","jquery.byteLimit"]],["ext.visualEditor.mwformatting",1548854100,["ext.visualEditor.mwcore"]],["ext.visualEditor.mwimage.core",1548854100,["ext.visualEditor.mwcore"]],[
"ext.visualEditor.mwimage",1548854100,["ext.visualEditor.mwimage.core"]],["ext.visualEditor.mwlink",1548854100,["ext.visualEditor.mwcore"]],["ext.visualEditor.mwmeta",1548854100,["ext.visualEditor.mwcore","ext.visualEditor.mwlink"]],["ext.visualEditor.mwreference.core",1548854100,["ext.visualEditor.mwcore"]],["ext.visualEditor.mwreference",1548854100,["ext.visualEditor.mwreference.core","ext.visualEditor.mwtransclusion"]],["ext.visualEditor.mwtransclusion.core",1548854100,["ext.visualEditor.mwcore"]],["ext.visualEditor.mwtransclusion",1548854100,["ext.visualEditor.mwtransclusion.core","mediawiki.jqueryMsg","mediawiki.language"]],["ext.visualEditor.language",1548854100,["ext.visualEditor.core","mediawiki.language.names"]],["ext.visualEditor.mwalienextension",1548854100,["ext.visualEditor.mwcore"]],["ext.visualEditor.mwgallery",1548854100,["ext.visualEditor.mwcore"]],["ext.visualEditor.experimental",1202225400,["ext.visualEditor.language","ext.visualEditor.mwalienextension"]],[
"ext.visualEditor.wikia.viewPageTarget.init",1548854100,["jquery.client","jquery.byteLength","mediawiki.Title","mediawiki.Uri","mediawiki.util","user.options","ext.visualEditor.track"]],["ext.visualEditor.wikia.oasisViewPageTarget",1548854100,["ext.visualEditor.viewPageTarget"]],["ext.visualEditor.wikia.core",1548854100,["ext.visualEditor.core.desktop","ext.visualEditor.mwimage","ext.visualEditor.mwmeta"]],["ext.closeMyAccount",1548854100,[],null,"local",["sass"]],["ext.TwitterTag",1548854100],["ext.wikia.VKTag",1548854100],["ext.ArticleVideo.jw",1548854100],["ext.fandomComMigration",1202225400],["ext.wikia.CategoryPage3.categoryLayoutSelector.scripts",1548854100],["ext.maps.common",1548854100,[],"ext.maps"],["ext.maps.coord",1548854100,[],"ext.maps"],["ext.maps.resizable",1202225400,["jquery.ui.resizable"],"ext.maps"],["mapeditor",1548854100,["ext.maps.common","jquery.ui.autocomplete","jquery.ui.slider","jquery.ui.dialog"],"ext.maps"],["ext.maps.services",1548854100,["ext.maps.common"
,"ext.maps.coord"],"ext.maps"],["ext.maps.googlemaps3",1548854100,["ext.maps.common"],"ext.maps"],["ext.maps.gm3.markercluster",1548854100,[],"ext.maps"],["ext.maps.gm3.markerwithlabel",1548854100,[],"ext.maps"],["ext.maps.gm3.geoxml",1548854100,[],"ext.maps/geoxml3"],["ext.maps.gm3.earth",1548854100,[],"ext.maps"],["ext.maps.openlayers",1548854100,["ext.maps.common"],"ext.maps"],["ext.maps.leaflet",1548854100,["ext.maps.common"],"ext.maps"],["ext.maps.leaflet.fullscreen",1548854100,["ext.maps.leaflet"],"ext.maps"],["ext.maps.leaflet.markercluster",1548854100,["ext.maps.leaflet"],"ext.maps"],["ext.maps.leaflet.providers",1548854100,["ext.maps.leaflet"],"ext.maps"]]);mw.config.set({"wgLoadScript":"/load.php","debug":!1,"skin":"oasis","stylepath":"https://slot1-images.wikia.nocookie.net/__cb7960017960012/common/skins","wgUrlProtocols":
"\\/\\/|ftp\\:\\/\\/|git\\:\\/\\/|gopher\\:\\/\\/|http\\:\\/\\/|https\\:\\/\\/|irc\\:\\/\\/|ircs\\:\\/\\/|mailto\\:|mms\\:\\/\\/|news\\:|nntp\\:\\/\\/|svn\\:\\/\\/|telnet\\:\\/\\/|worldwind\\:\\/\\/|xmpp\\:","wgArticlePath":"/wiki/$1","wgScriptPath":"","wgScriptExtension":".php","wgScript":"/index.php","wgVariantArticlePath":!1,"wgActionPaths":{},"wgServer":"https://borderlands.fandom.com","wgUserLanguage":"en","wgContentLanguage":"en","wgVersion":"1.19.24","wgEnableAPI":!0,"wgEnableWriteAPI":!0,"wgDefaultDateFormat":"mdy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgMainPageTitle":"Borderlands Wiki","wgFormattedNamespaces":{"-2":"Media","-1":"Special","0":"","1":"Talk","2":"User","3":"User talk","4":"Borderlands Wiki","5":"Borderlands Wiki talk","6":"File","7":"File talk","8":"MediaWiki","9":
"MediaWiki talk","10":"Template","11":"Template talk","12":"Help","13":"Help talk","14":"Category","15":"Category talk","110":"Forum","111":"Forum talk","500":"User blog","501":"User blog comment","502":"Blog","503":"Blog talk","828":"Module","829":"Module talk","1200":"Message Wall","1201":"Thread","1202":"Message Wall Greeting","2000":"Board","2001":"Board Thread","2002":"Topic"},"wgNamespaceIds":{"media":-2,"special":-1,"":0,"talk":1,"user":2,"user_talk":3,"borderlands_wiki":4,"borderlands_wiki_talk":5,"file":6,"file_talk":7,"mediawiki":8,"mediawiki_talk":9,"template":10,"template_talk":11,"help":12,"help_talk":13,"category":14,"category_talk":15,"forum":110,"forum_talk":111,"user_blog":500,"user_blog_comment":501,"blog":502,"blog_talk":503,"module":828,"module_talk":829,"message_wall":1200,"thread":1201,"message_wall_greeting":1202,"board":2000,"board_thread":2001,"topic":2002,"image":6,"image_talk":7,"project":4,"project_talk":5},"wgSiteName":"Borderlands Wiki","wgFileExtensions":
["png","gif","jpg","jpeg","ico","pdf","svg","odt","ods","odp","odg","odc","odf","odi","odm","ogg","ogv","oga"],"wgDBname":"borderlands","wgFileCanRotate":!0,"wgAvailableSkins":{"oasis":"Oasis","wikiamobile":"WikiaMobile"},"wgExtensionAssetsPath":"/extensions","wgCookiePrefix":"wikicities","wgResourceLoaderMaxQueryLength":-1,"wgCaseSensitiveNamespaces":[],"wgLegalTitleChars":" %!\"$\x26\'()*,\\-./0-9:;=?@A-Z\\\\\\^_`a-z~+\\u0080-\\uFFFF","wgSassParams":{"background-dynamic":"true","background-image":"https://static1.wikia.nocookie.net/borderlands/images/5/50/Wiki-background","background-image-height":"600","background-image-width":"1700","color-body":"#000000","color-body-middle":"#000000","color-buttons":"#891100","color-community-header":"#891100","color-header":"darkorange","color-links":"#fec356","color-page":"#000000","oasisTypography":1,"page-opacity":"100","widthType":0,"wordmark-font":"megalopolis"},"wgWikiaBaseDomain":"wikia.com","wgWikiaBaseDomainRegex":
"((wikia|fandom)\\.com|(wikia|fandom)-dev\\.(com|us|pl))","wgServicesExternalDomain":"https://services.fandom.com/","wgServicesExternalAlternativeDomain":"https://services.wikia.com/","wgRecommendedVideoABTestPlaylist":"","wgJSMessagesCB":"7960017960012.0.0","wgVisualEditorConfig":{"disableForAnons":!1,"preferenceModules":{"visualeditor-enable-experimental":"ext.visualEditor.experimental","visualeditor-enable-language":"ext.visualEditor.language"},"namespaces":[0,2,14,4],"pluginModules":["ext.visualEditor.wikia.core"],"defaultUserOptions":{"betatempdisable":0,"enable":1,"defaultthumbsize":180,"visualeditor-enable-experimental":0,"visualeditor-enable-language":0},"blacklist":{"msie":null,"android":[["\x3c",3]],"firefox":[["\x3c=",14]],"opera":[["\x3c",12]],"blackberry":null,"silk":null},"skins":["oasis","venus"],"tabPosition":"before","tabMessages":{"edit":null,"editsource":"visualeditor-ca-classiceditor","create":null,"createsource":"visualeditor-ca-classiceditor",
"editlocaldescriptionsource":"visualeditor-ca-editlocaldescriptionsource","createlocaldescriptionsource":"visualeditor-ca-createlocaldescriptionsource","editsection":null,"editsectionsource":"visualeditor-ca-editsource-section","editappendix":null,"editsourceappendix":null,"createappendix":null,"createsourceappendix":null,"editsectionappendix":null,"editsectionsourceappendix":null},"showBetaWelcome":!1,"enableTocWidget":!1},"wgCommunityPageDisableTopContributors":!1});mw.loader.state({"jquery":"ready"});window.preMwLdrSt&&mw.loader.state(window.preMwLdrSt);if(window.preMwLdrStA){for(var i=0;i<window.preMwLdrStA.length;i++)mw.loader.state(window.preMwLdrStA[i]);};};if(isCompatible()){document.write("\x3cscript src=\"https://slot1-images.wikia.nocookie.net/__load/-/debug%3Dfalse%26lang%3Den%26only%3Dscripts%26skin%3Doasis%26version%3D7960017960012-20190130T131500Z/jquery,mediawiki\"\x3e\x3c/script\x3e");}delete isCompatible;;

/* cache key: borderlands:resourceloader:filter:minify-js:7:e6a400c24c18df6d710ba888f86460e5 */
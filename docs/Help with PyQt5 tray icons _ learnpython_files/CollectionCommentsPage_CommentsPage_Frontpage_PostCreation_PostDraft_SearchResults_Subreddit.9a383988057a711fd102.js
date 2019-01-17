(window.webpackJsonp=window.webpackJsonp||[]).push([["CollectionCommentsPage~CommentsPage~Frontpage~PostCreation~PostDraft~SearchResults~Subreddit"],{"./src/reddit/components/CreatePostButton/index.tsx":function(e,t,n){"use strict";var o=n("./node_modules/react/index.js"),i=n.n(o),r=n("./node_modules/react-redux/es/index.js"),s=n("./src/app/strings/index.ts"),d=n("./src/reddit/actions/modal.ts"),a=n("./src/reddit/constants/modals.ts"),c=n("./src/reddit/constants/page.ts"),l=n("./src/reddit/controls/Button/index.tsx"),p=n("./src/reddit/helpers/getSubredditUrl/index.ts"),u=n("./src/reddit/selectors/telemetry.ts"),g=n("./src/reddit/selectors/user.ts"),m=n("./node_modules/reselect/lib/index.js"),b=n("./src/reddit/components/TrackingHelper/index.tsx"),f=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(e[o]=n[o])}return e},h=function(e,t){var n={};for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&t.indexOf(o)<0&&(n[o]=e[o]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols){var i=0;for(o=Object.getOwnPropertySymbols(e);i<o.length;i++)t.indexOf(o[i])<0&&(n[o[i]]=e[o[i]])}return n};const y=Object(m.createStructuredSelector)({isLoggedIn:g.D,language:g.J}),x=Object(r.connect)(y,e=>({openLoginModal:()=>e(Object(d.j)(a.a.REGISTER_MODAL_ID))}));t.a=x(Object(b.b)(e=>{var t=e.isLoggedIn,n=e.language,o=e.listingName,r=e.openLoginModal,d=e.sendEvent,a=e.subreddit,g=h(e,["isLoggedIn","language","listingName","openLoginModal","sendEvent","subreddit"]);return i.a.createElement(l.f,f({},g,{onClick:e=>{d(e=>({action:"click",noun:"create_post",source:"id_card",screen:Object(u.screen)(e),subreddit:Object(u.subreddit)(e),actionInfo:Object(u.actionInfo)(e)})),t||(r(),e.preventDefault())},to:`${Object(p.a)(a)||(e=>e===c.j?"/original/":"")(o)||"/"}submit`}),Object(s.a)(n,"postCreation.createPost"))}))},"./src/reddit/components/IdCard/Placeholder.tsx":function(e,t,n){"use strict";var o,i=n("./node_modules/react/index.js"),r=n.n(i),s=n("./bundled-modules/styled-components/styled-components.min.js"),d=n.n(s),a=n("./src/lib/classNames/index.ts"),c=n("./src/reddit/helpers/styles/mixins/loading.ts"),l=n("./src/reddit/models/Theme/NewColorSystem/index.ts"),p=n("./src/reddit/components/IdCard/placeholder.m.less"),u=n.n(p),g=(o="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103,function(e,t,n,i){var r=e&&e.defaultProps,s=arguments.length-3;if(t||0===s||(t={}),t&&r)for(var d in r)void 0===t[d]&&(t[d]=r[d]);else t||(t=r||{});if(1===s)t.children=i;else if(s>1){for(var a=Array(s),c=0;c<s;c++)a[c]=arguments[c+3];t.children=a}return{$$typeof:o,type:e,key:void 0===n?null:""+n,ref:null,props:t,_owner:null}}),m=function(e,t){var n={};for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&t.indexOf(o)<0&&(n[o]=e[o]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols){var i=0;for(o=Object.getOwnPropertySymbols(e);i<o.length;i++)t.indexOf(o[i])<0&&(n[o[i]]=e[o[i]])}return n};const b=d()(e=>{e.isLoading,e.gradientType;var t=m(e,["isLoading","gradientType"]);return r.a.createElement("div",t)}).withConfig({componentId:"s1lp57jt-0"})(["",""],c.b),f=d.a.div.withConfig({componentId:"s1lp57jt-1"})(["background-color: ",";"],e=>Object(l.c)(e).widgetColors.sidebarWidgetBackgroundColor);t.a=(({isLoading:e})=>g(f,{className:u.a.container},void 0,g(b,{gradientType:"posts",isLoading:e,className:u.a.banner}),g("div",{className:u.a.title},void 0,g(b,{gradientType:"posts",isLoading:e,className:u.a.icon}),g(b,{gradientType:"posts",isLoading:e,className:u.a.name})),g("div",{className:u.a.counts},void 0,g("div",{className:u.a.side},void 0,g(b,{gradientType:"posts",isLoading:e,className:u.a.count}),g(b,{gradientType:"posts",isLoading:e,className:u.a.text})),g("div",{className:u.a.side},void 0,g(b,{gradientType:"posts",isLoading:e,className:u.a.count}),g(b,{gradientType:"posts",isLoading:e,className:u.a.text}))),g(b,{gradientType:"posts",isLoading:e,className:Object(a.a)(u.a.desc,u.a.one)}),g(b,{gradientType:"posts",isLoading:e,className:Object(a.a)(u.a.desc,u.a.two)}),g(b,{gradientType:"posts",isLoading:e,className:Object(a.a)(u.a.desc,u.a.three)}),g(b,{gradientType:"posts",isLoading:e,className:Object(a.a)(u.a.desc,u.a.four)}),g(b,{gradientType:"posts",isLoading:e,className:u.a.subscribe})))},"./src/reddit/components/IdCard/index.m.less":function(e,t,n){e.exports={categoryContainer:"_37coyt0h8ryIQubA7RHmUc",icon:"_2XJvPvYIEYtcS4ORsDXwa3",subredditIcon:"_2Vkdik1Q8k0lBEhhA_lRKE",largeSubredditIcon:"eGjjbHtkgFc-SYka3LM3M",planetIcon:"ZtU5GBgjF1m_LMGdL3d7x",largePlanetIcon:"_3mmJ1GWMWurrNWGlAosDIq"}},"./src/reddit/components/IdCard/index.tsx":function(e,t,n){"use strict";var o=n("./node_modules/react/index.js"),i=n.n(o),r=n("./node_modules/react-redux/es/index.js"),s=n("./node_modules/react-router-dom/es/index.js"),d=n("./node_modules/react-router-redux/es/index.js"),a=n("./node_modules/reselect/lib/index.js"),c=n("./bundled-modules/styled-components/styled-components.min.js"),l=n.n(c),p=n("./src/app/strings/index.ts"),u=n("./src/lib/isFakeSubreddit/index.ts"),g=n("./src/lib/prettyPrintNumber/index.ts"),m=n("./src/app/actions/tooltip.ts"),b=n("./src/reddit/components/CategoryTagList/index.tsx"),f=n("./src/reddit/components/CreateCommunityButton/index.tsx"),h=n("./src/reddit/components/CreatePostButton/index.tsx"),y=n("./src/reddit/components/InfoTextTooltip/index.tsx"),x=n("./src/higherOrderComponents/addOverlayEvents.tsx"),v=n("./src/higherOrderComponents/asTooltip.tsx"),w=n("./src/reddit/actions/monthsToMinutes.ts"),O=n("./src/reddit/constants/componentSizes.ts"),j=n("./src/reddit/constants/zIndex.ts"),C=n("./src/reddit/models/MonthsToMinutes/index.ts"),I=n("./src/reddit/components/MonthsToMinutesTooltip/index.tsx"),k=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(e[o]=n[o])}return e};const S=Object(v.a)(l()(I.a).withConfig({componentId:"tnff3g-0"})(["","margin-left: -8px;margin-top: ","px;;z-index: ",";&:before {left: initial;right: -.5em;top: 16px;}"],"",e=>e.isOverlay?-O.h:0,j.m+1),[x.a.Click,x.a.Keydown,x.a.Resize]);var T,N=Object(r.connect)(null,e=>({onTooltipActivated:t=>e(Object(w.x)({time:Date.now(),tooltipType:t}))}))(class extends i.a.Component{componentDidMount(){this.props.isOpen&&this.props.onTooltipActivated(C.i.SubscribeIdCard)}render(){const e=this.props;return i.a.createElement(S,k({targetPosition:["left","top"],tooltipPosition:["right","top"],tooltipType:C.i.SubscribeIdCard},e))}}),_=n("./src/reddit/actions/authorFlair.ts"),P=n("./src/reddit/actions/badge.ts"),B=n("./src/reddit/components/Badges/UserDisplay/index.tsx"),F=n("./src/reddit/components/Flair/index.tsx"),L=n("./src/reddit/components/TrackingHelper/index.tsx"),$=n("./src/reddit/controls/Button/index.tsx"),q=n("./src/reddit/featureFlags/index.ts"),A=n("./src/reddit/featureFlags/component.tsx"),E=n("./src/reddit/helpers/styles/mixins/fonts.tsx"),W=n("./src/reddit/helpers/trackers/lightbox.ts"),H=n("./src/reddit/models/Theme/NewColorSystem/index.ts"),M=n("./src/reddit/models/User/index.ts"),D=n("./src/reddit/selectors/user.ts"),z=n("./src/reddit/selectors/userFlair.ts"),U=n("./src/reddit/components/SidebarFlairSettings/index.m.less"),J=n.n(U),R=(T="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103,function(e,t,n,o){var i=e&&e.defaultProps,r=arguments.length-3;if(t||0===r||(t={}),t&&i)for(var s in i)void 0===t[s]&&(t[s]=i[s]);else t||(t=i||{});if(1===r)t.children=o;else if(r>1){for(var d=Array(r),a=0;a<r;a++)d[a]=arguments[a+3];t.children=d}return{$$typeof:T,type:e,key:void 0===n?null:""+n,ref:null,props:t,_owner:null}});const V=l.a.div.withConfig({componentId:"naa87w-0"})(["border-top: 1px solid ",";margin-top: 12px;padding-top: 12px;"],e=>Object(H.c)(e).widgetColors.lineColor),Q=l.a.div.withConfig({componentId:"naa87w-1"})(["","align-items: center;background-color: ",";border-radius: 4px;display: flex;flex-direction: row;margin: 8px 0;padding: 8px;"],E.metadataFont,e=>Object(H.c)(e).body),G=l.a.div.withConfig({componentId:"naa87w-2"})(["",""],E.labelsFont),X=l()(F.c).withConfig({componentId:"naa87w-3"})(["margin-left: 8px;"]),K=l()($.l).withConfig({componentId:"naa87w-4"})(["display: flex;margin-left: auto;"]),Y=l.a.span.withConfig({componentId:"naa87w-5"})(["color: ",";flex: 0 0 auto;line-height: 16px;"],e=>Object(H.c)(e).bodyText),Z=Object(A.a)("spBadges",B.a),ee=Object(a.createStructuredSelector)({badgesEnabled:q.d.spBadges,currentUser:D.j,language:D.J,userFlairData:z.b,userHasBadge:(e,t)=>{const n=e.user.account;if(n){return!!((e.users.appliedBadges[n.id]||{})[t.subredditId]||[]).length}return!1}}),te=Object(r.connect)(ee,(e,{subredditId:t})=>({onToggleModal:n=>e(Object(_.b)({username:n,subredditId:t})),onToggleBadgeModal:()=>e(Object(P.j)())})),ne=e=>R(K,{onClick:e.onClick},void 0,e.userFlairData.applied?Object(p.a)(e.language,"flair.editUserFlair"):Object(p.a)(e.language,"flair.addUserFlair")),oe=e=>R(K,{onClick:e.onClick},void 0,e.userFlairData.displaySettings.isEnabled?e.userFlairData.applied||e.userHasBadge?Object(p.a)(e.language,"flair.editUserFlairAndBadge"):Object(p.a)(e.language,"flair.addUserFlairAndBadge"):e.userHasBadge?Object(p.a)(e.language,"flair.editUserBadge"):Object(p.a)(e.language,"flair.addUserBadge"));var ie=te(Object(L.b)(class extends i.a.Component{constructor(){super(...arguments),this.onFlairLinkClick=(()=>{const e=this.props.currentUser?Object(M.e)(this.props.currentUser):null;this.props.onToggleModal(e),this.props.sendEvent(Object(W.a)("user_flair_picker"))})}render(){var e=this.props;const t=e.badgesEnabled,n=e.currentUser,o=e.language,i=e.onToggleBadgeModal,r=e.subredditId,s=e.userFlairData,d=e.userHasBadge;return n&&s?R(V,{},void 0,R(G,{},void 0,Object(p.a)(o,"flair.preview")),R(Q,{},void 0,d&&R(Z,{className:J.a.badge,subredditId:r,uniqueIdentifier:r}),R(Y,{},void 0,`u/${n.displayText}`),s.applied&&s.displaySettings.isUserEnabled&&R(X,{flair:s.applied,forceSmallEmojis:!0})),t?R(oe,{userFlairData:s,userHasBadge:d,language:o,onClick:i}):s.displaySettings.isEnabled&&R(ne,{userFlairData:s,language:o,onClick:this.onFlairLinkClick})):null}})),re=n("./src/reddit/components/SubscribeButton/index.tsx"),se=n("./src/reddit/components/Widgets/Base/index.tsx"),de=n("./src/reddit/components/Widgets/ThemedWidget/index.tsx"),ae=n("./src/reddit/constants/colors.ts"),ce=n("./src/reddit/constants/elementIds.ts"),le=n("./src/reddit/constants/listings.ts"),pe=n("./src/reddit/constants/page.ts"),ue=n("./src/reddit/helpers/styles/components/index.tsx"),ge=n("./src/reddit/helpers/styles/mixins/index.tsx"),me=n("./src/reddit/helpers/trackers/modHub.ts"),be=n("./src/reddit/icons/fonts/helpers.tsx"),fe=function(){var e="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103;return function(t,n,o,i){var r=t&&t.defaultProps,s=arguments.length-3;if(n||0===s||(n={}),n&&r)for(var d in r)void 0===n[d]&&(n[d]=r[d]);else n||(n=r||{});if(1===s)n.children=i;else if(s>1){for(var a=Array(s),c=0;c<s;c++)a[c]=arguments[c+3];n.children=a}return{$$typeof:e,type:t,key:void 0===o?null:""+o,ref:null,props:n,_owner:null}}}();var he=l()(e=>fe("i",{className:`${Object(be.b)("modSettings")} ${e.className}`})).withConfig({componentId:"s1nioeso-0"})(["display: inline-block;vertical-align: text-bottom;width: 16px;height: 16px;font-size: 16px;line-height: 16px;"]),ye=n("./src/reddit/icons/svgs/CircledPlanet/index.tsx"),xe=n("./src/reddit/icons/svgs/QuarantineWarning/index.tsx"),ve=n("./node_modules/polished/dist/polished.es.js"),we=function(){var e="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103;return function(t,n,o,i){var r=t&&t.defaultProps,s=arguments.length-3;if(n||0===s||(n={}),n&&r)for(var d in r)void 0===n[d]&&(n[d]=r[d]);else n||(n=r||{});if(1===s)n.children=i;else if(s>1){for(var a=Array(s),c=0;c<s;c++)a[c]=arguments[c+3];n.children=a}return{$$typeof:e,type:t,key:void 0===o?null:""+o,ref:null,props:n,_owner:null}}}();var Oe=l()(e=>we("svg",{className:e.className,xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 20 20"},void 0,we("path",{d:"M17.71,10.29,14.95,7.54a7,7,0,0,0-9.9,0L2.29,10.29a1,1,0,0,0,1.41,1.41L6.46,8.95c.07-.07.14-.11.21-.17a4,4,0,1,0,6.65,0c.07.06.15.11.21.17l2.76,2.76a1,1,0,0,0,1.41-1.41Z"}))).withConfig({componentId:"hauj45-0"})(["fill: ",";"],e=>Object(ve.f)(.6,Object(H.c)(e).active)),je=n("./src/reddit/models/Subreddit/index.ts"),Ce=n("./src/reddit/models/Theme/index.ts"),Ie=n("./src/reddit/selectors/category.ts"),ke=n("./src/reddit/selectors/comments.ts"),Se=n("./src/reddit/selectors/experiments/categories.ts"),Te=n("./src/reddit/selectors/listings.ts"),Ne=n("./src/reddit/selectors/moderatorPermissions.ts"),_e=n("./src/reddit/selectors/monthsToMinutes.ts"),Pe=n("./src/reddit/selectors/structuredStyles.ts"),Be=n("./src/reddit/selectors/subreddit.ts"),Fe=n("./src/reddit/selectors/widgets.ts"),Le=n("./src/config.ts");const $e=e=>e&&e.toLowerCase()===le.b.Popular,qe=e=>e&&e.toLowerCase()===le.b.All,Ae=e=>e&&e===pe.c,Ee=e=>e&&e===pe.j,We=(e,t=40,n=68)=>({height:n,image:e,width:t}),He=({language:e,listingName:t,subreddit:n,idCardWidget:o})=>{let i,r,s,d,a,c;const l=o&&o.subscribersText||Object(p.a)(e,"structuredStyles.widgets.id-card.subscribersText"),u=o&&o.currentlyViewingText||Object(p.a)(e,"structuredStyles.widgets.id-card.currentlyViewingText");let g,m;if(Ae(t)){i=`${Le.a.assetPath}/img/id-cards/home-banner@2x.png`,r=Object(p.a)(e,"listings.home.longDescription"),s=We(`url('${Le.a.assetPath}/img/id-cards/snoo-home@2x.png')`);const t=Object(p.a)(e,"listings.home.title");d=t.charAt(0).toUpperCase()+t.slice(1),c=le.c[le.b.Home]}else if(qe(t))i=`${Le.a.assetPath}/img/id-cards/banner@2x.png`,r=Object(p.a)(e,"listings.all.longDescription"),s=We(`url('${Le.a.assetPath}/img/id-cards/snoo-home@2x.png')`),d="r/all",c=le.c[le.b.All];else if(Ee(t)){i=`${Le.a.assetPath}/img/id-cards/oc-banner@2x.png`,r=Object(p.a)(e,"listings.originalContent.longDescription"),s=We(`url('${Le.a.assetPath}/img/id-cards/snoo-oc@2x.png')`,68);const t=Object(p.a)(e,"listings.originalContent.title");d=t.charAt(0).toUpperCase()+t.slice(1),a=Object(p.a)(e,"listings.originalContent.titleSecondary"),c=le.c[le.b.Original]}else $e(t)?(i=`${Le.a.assetPath}/img/id-cards/banner@2x.png`,r=Object(p.a)(e,"listings.popular.longDescription"),s=We(`url('${Le.a.assetPath}/img/id-cards/snoo-home@2x.png')`),d="r/popular",c=le.c[le.b.Popular]):t&&(r=o&&o.description,s=We(""),d=n.displayText,c=n.url,m=o&&o.subscribersCount,g=o&&o.currentlyViewingCount);return Object.assign({snooBackground:s,description:r,titleText:d,titleSecondaryText:a,url:c,subscribersCount:m,subscribersText:l,currentlyViewingText:u,currentlyViewingCount:g},i?{bannerBackgroundImage:i}:{})};var Me=n("./src/reddit/components/IdCard/Placeholder.tsx"),De=n("./src/reddit/components/IdCard/index.m.less"),ze=n.n(De);n.d(t,"d",function(){return Re}),n.d(t,"a",function(){return ct}),n.d(t,"b",function(){return Ct}),n.d(t,!1,function(){return Me.a});var Ue=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(e[o]=n[o])}return e},Je=function(){var e="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103;return function(t,n,o,i){var r=t&&t.defaultProps,s=arguments.length-3;if(n||0===s||(n={}),n&&r)for(var d in r)void 0===n[d]&&(n[d]=r[d]);else n||(n=r||{});if(1===s)n.children=i;else if(s>1){for(var a=Array(s),c=0;c<s;c++)a[c]=arguments[c+3];n.children=a}return{$$typeof:e,type:t,key:void 0===o?null:""+o,ref:null,props:n,_owner:null}}}();const Re=e=>!Object(u.a)(e)||qe(e)||Ae(e)||$e(e)||Ee(e),Ve=l()(Object(ue.a)()).withConfig({componentId:"s1pyq7tn-0"})(["background: ",";border-radius: 4px 4px 0 0;height: 34px;margin: -12px -12px 10px;"],e=>Object(Ce.g)(Object(H.c)(e).active,e.bannerBackgroundImage||Object(H.c)(e).banner.backgroundImage,"cover")),Qe=l.a.div.withConfig({componentId:"s1pyq7tn-1"})(["align-items: center;display: flex;& > * {display: inline-block;vertical-align: middle;}"]),Ge=l()(Qe).withConfig({componentId:"s1pyq7tn-2"})(["margin-top: -23px;"]),Xe=l()(Object(ue.a)()).withConfig({componentId:"s1pyq7tn-3"})(["background: ",";background-size: ","px ","px;display: inline-block;flex-shrink: 0;height: ","px;position: relative;width: ","px;"],e=>e.snooBackground.image,e=>e.snooBackground.width,e=>e.snooBackground.height,e=>e.snooBackground.height,e=>e.snooBackground.width),Ke=Object(c.css)(["background: ",";border: 2px solid ",";"],e=>Object(H.c)(e).active,e=>Object(H.c)(e).line),Ye=l()(Object(ue.a)()).withConfig({componentId:"s1pyq7tn-4"})(["",";background-image: url('","');",""],Ke,e=>e.url,e=>e.primaryColor?`background-color: ${e.primaryColor};`:""),Ze=l()(ye.a).withConfig({componentId:"s1pyq7tn-5"})(["",";border: 2px solid ",";fill: ",";",";"],Ke,e=>Object(H.c)(e).lightText,e=>Object(H.c)(e).lightText,e=>e.primaryColor?`background: ${e.primaryColor};`:""),et=l()(s.a).withConfig({componentId:"s1pyq7tn-6"})(["flex: 1 1 auto;overflow: hidden;text-overflow: ellipsis;&:hover {text-decoration: underline;}"]),tt=l.a.span.withConfig({componentId:"s1pyq7tn-7"})(["","display: inline-block;"],E.titleFontH4),nt=l.a.div.withConfig({componentId:"s1pyq7tn-8"})(["margin-left: 10px;margin-top: ","px;"],e=>e.hasSecondaryTitle?35:30),ot=l()(tt).withConfig({componentId:"s1pyq7tn-9"})(["color: ",";",""],e=>Object(H.c)(e).actionIcon,E.metadataFont),it=l.a.div.withConfig({componentId:"s1pyq7tn-10"})(["display: flex;margin: 8px 0;& > * {flex: 1;}"]),rt=l.a.div.withConfig({componentId:"s1pyq7tn-11"})(["border-left: 1px solid ",";padding-left: 12px;"],e=>Object(H.c)(e).widgetColors.lineColor),st=l.a.p.withConfig({componentId:"s1pyq7tn-12"})(["",""],E.titleFontH4),dt=l.a.p.withConfig({componentId:"s1pyq7tn-13"})(["","display: inline-block;word-break: break-word;"],E.titleFontH6),at=l()(se.a).withConfig({componentId:"s1pyq7tn-14"})(["margin-top: 10px;"]),ct=l.a.p.withConfig({componentId:"s1pyq7tn-15"})(["","margin-top: 8px;word-wrap: break-word;"],E.bodyFont),lt=l.a.div.withConfig({componentId:"s1pyq7tn-16"})(["margin-top: 12px;"]),pt="\n  display: block;\n  width: 100%;\n",ut=l()(re.a).withConfig({componentId:"s1pyq7tn-17"})(["",";margin-bottom: 8px;"],pt),gt=l()(h.a).withConfig({componentId:"s1pyq7tn-18"})(["",";","padding: 0 16px;"],pt,E.largeButtonFont),mt=l()(f.a).withConfig({componentId:"s1pyq7tn-19"})(["",";","margin-top: 11px;"],ge.e,E.largeButtonFont),bt=l()(he).withConfig({componentId:"s1pyq7tn-20"})(["margin-right: 4px;vertical-align: middle;"]),ft=l()(s.a).withConfig({componentId:"s1pyq7tn-21"})(["border-radius: 4px;margin: 6px 0px 6px auto;padding: 4px;"]),ht=Object(c.css)(["","color: ",";text-transform: uppercase;"],E.bodyFontSmall,e=>Object(H.c)(e).metaText),yt=l.a.div.withConfig({componentId:"s1pyq7tn-22"})(["",""],ht),xt=l()(Oe).withConfig({componentId:"s1pyq7tn-23"})(["display: inline-block;fill: ",";height: 20px;margin-right: 4px;vertical-align: bottom;"],e=>Object(H.c)(e).metaText),vt=l.a.div.withConfig({componentId:"s1pyq7tn-24"})(["","& > svg {display: inline-block;fill: ",";height: 12px;margin-right: 4px;vertical-align: middle;}"],ht,ae.a.quarantine),wt=l.a.div.withConfig({componentId:"s1pyq7tn-25"})(["border-top: 1px solid ",";margin-top: 10px;"],e=>Object(H.c)(e).widgetColors.lineColor),Ot=Object(r.connect)(()=>Object(a.createStructuredSelector)({postCategories:(e,t)=>Object(Ie.n)(e,t.postId),commentsApiError:ke.c,commentsApiPending:ke.d,frontpageIsHome:_e.i,idCardWidget:(e,t)=>Object(Fe.c)(e,{subredditName:t.listingName}),isLoggedIn:D.D,language:D.J,listingApiError:Te.c,listingApiPending:Te.d,moderatorPermissions:(e,t)=>{const n=Object(Be.z)(e,t.listingName);if(n)return Object(Ne.g)(e,{subredditId:n})},isInCategoriesExperiment:Se.a,subreddit:(e,t)=>Object(Be.w)(e,{subredditName:t.listingName}),subredditIcon:(e,t)=>Object(Pe.n)(e,{subredditName:t.listingName}),subscribeIdTooltipIsOpen:_e.s}),(e,t)=>({dispatchPush:t=>e(Object(d.b)(t)),toggleTooltip:t=>e(Object(m.e)({tooltipId:t}))}),(e,t,n)=>Object.assign({},e,t,n,{onContainerClick:()=>n.isOverlay&&t.dispatchPush(e.subreddit.url)}));const jt=({titleText:e,titleSecondaryText:t,snooBackground:n})=>Je(Ge,{},void 0,Je(Xe,{snooBackground:n}),Je(nt,{hasSecondaryTitle:!!t},void 0,Je(tt,{},void 0,e),t&&Je(ot,{},void 0,t))),Ct=e=>{const t=e.isTargetBlank,n=e.largeSubredditIcon,o=e.linkUrl,r=e.subredditIcon,s=e.titleText,d=e.primaryColor;return Je(Qe,{className:e.className},void 0,r.url?Je(Ye,{className:n?ze.a.largeSubredditIcon:ze.a.subredditIcon,url:r.url,primaryColor:d},r.url):Je(Ze,{primaryColor:d,className:n?ze.a.largePlanetIcon:ze.a.planetIcon},"planet"),o?i.a.createElement(et,Ue({key:o,to:o,onClick:e=>e.stopPropagation()},t?{target:"_blank"}:{}),Je(tt,{title:s},void 0,s)):Je(tt,{},s,s))},It=(e,t,n,o,i,r,s,d)=>Je(it,{},void 0,Je("div",{onMouseEnter:()=>d(o),onMouseLeave:()=>d(o)},void 0,Je(st,{},void 0,Object(g.b)(t)),Je(dt,{id:o},void 0,n),Je(y.b,{caretOnTop:!0,text:`${Object(g.b)(t,!0)} ${n}`,tooltipId:o})),Je(rt,{onMouseEnter:()=>d(s),onMouseLeave:()=>d(s)},void 0,Je(st,{},void 0,Object(g.b)(i)),Je(dt,{id:s},void 0,r),Je(y.b,{caretOnTop:!0,text:`${Object(g.b)(i,!0)} ${r}`,tooltipId:s}))),kt=e=>Je(ct,{},void 0,e),St=({isFake:e,isOverlay:t,isLoggedIn:n,isSubmissionPage:o,language:i,listingName:r,subreddit:s})=>Je(lt,{},void 0,!e&&Je(ut,{getEventFactory:e=>Object(W.a)(e?"unsubscribe":"subscribe"),id:`subscribe-button-${s.id}`,identifier:{name:s.name,type:"subreddit"},onClick:e=>e.stopPropagation()}),!o&&!t&&Je(gt,{listingName:r,subreddit:s}),n&&!o&&!t&&!s&&r!==pe.j&&Je(mt,{eventSource:"id_card",language:i}));t.c=Object(L.b)(Ot(Object(c.withTheme)(class extends i.a.Component{constructor(){super(...arguments),this.onClickModTools=(()=>this.props.sendEvent(Object(me.a)()))}render(){var e=this.props;const t=e.className,n=e.commentsApiError,o=e.commentsApiPending,r=e.frontpageIsHome,s=e.language,d=e.listingApiError,a=e.listingApiPending,c=e.listingName,l=e.idCardWidget,g=e.isCommentsPage,m=e.isLoggedIn,f=e.isOverlay,h=e.isSubmissionPage,y=e.moderatorPermissions,x=e.onContainerClick,v=e.postCategories,w=e.postId,O=e.isInCategoriesExperiment,j=e.subreddit,C=e.subredditIcon,I=e.subscribeIdTooltipIsOpen,k=e.toggleTooltip;let S=c;m||c!==pe.c||r||(S=le.b.Popular);const T=Object(u.a)(S);if(!T&&!l)return Je(Me.a,{isLoading:o&&!n||a&&!d});var _=He({language:s,listingName:S,subreddit:j,idCardWidget:l});const P=_.bannerBackgroundImage,B=_.currentlyViewingCount,F=_.currentlyViewingText,L=_.description,$=_.snooBackground,q=_.subscribersCount,A=_.subscribersText,E=_.titleText,W=_.titleSecondaryText,H=_.url,M=T||f||h,D=!T&&j.id?j.id:"",z=`IdCard--Subscribers--${f}--${D}`,U=`IdCard--CurrentlyViewing--${f}--${D}`;return Je(i.a.Fragment,{},void 0,Je(de.a,{className:t,onClick:f?x:void 0,headerButton:!M&&j&&y&&Je(ft,{to:y.posts?`${j.url}about/modqueue`:`${j.url}about/`,onClick:this.onClickModTools},void 0,Je(bt,{}),Object(p.a)(s,"modTools.modTools")),redditStyle:T||h,title:M?void 0:Object(p.a)(s,"sidebar.subreddit.title")},void 0,M&&Je(Ve,{bannerBackgroundImage:P}),T?jt({titleText:E,titleSecondaryText:W,snooBackground:$}):Je(Ct,{isTargetBlank:h,linkUrl:T?void 0:H,subredditIcon:C,titleText:E}),!T&&It(s,q,A,z,B,F,U,k),!T&&j.type===je.b.EmployeesOnly&&Je(yt,{},void 0,Je(xt,{}),j.allowContractors?Object(p.a)(s,"sidebar.subreddit.employeesAndContractors"):Object(p.a)(s,"sidebar.subreddit.employeesOnly")),j&&j.isQuarantined&&Je(vt,{},void 0,Je(xe.a,{}),Object(p.a)(s,"sidebar.subreddit.quarantined")),kt(L),St({isFake:T,isLoggedIn:m,isOverlay:f,isSubmissionPage:h,language:s,listingName:S,subreddit:j}),O&&v&&w&&(g||f)&&Je(wt,{},void 0,Je(at,{},void 0,Object(p.a)(s,"sidebar.categoryTag.discoverMore")),Je(b.a,{postId:w,inLightboxHeader:!0,postCategories:v})),!T&&!f&&Je(ie,{subredditId:j.id})),!T&&Je(N,{container:f?document.getElementById(ce.c):null,isOpen:I,isOverlay:f,tooltipId:`subscribe-button-${j.id}`}))}})))},"./src/reddit/components/IdCard/placeholder.m.less":function(e,t,n){e.exports={container:"_1KWSZXqSM_BLhBzkPyJFGR",banner:"c_dVyWK3BXRxSN3ULLJ_t",title:"_1OQL3FCA9BfgI57ghHHgV3",icon:"_33jgwegeMTJ-FJaaHMeOjV",name:"_1wQQNkVR4qNpQCzA19X4B6",counts:"_39IvqNe6cqNVXcMFxFWFxx",side:"_29TSdL_ZMpyzfQ_bfdcBSc",count:"JEV9fXVlt_7DgH-zLepBH",text:"_3YCOmnWpGeRBW_Psd5WMPR",desc:"_2iO5zt81CSiYhWRF9WylyN",one:"_2E9u5XvlGwlpnzki78vasG",two:"fDElwzn43eJToKzSCkejE",three:"_2kNB7LAYYqYdyS85f8pqfi",four:"_1XmngqAPKZO_1lDBwcQrR7",subscribe:"_3XbVvl-zJDbcDeEdSgxV4_"}},"./src/reddit/components/SidebarFlairSettings/index.m.less":function(e,t,n){e.exports={badge:"_2a172ppKObqWfRHr8eWBKV"}},"./src/reddit/components/SidebarFooter/index.tsx":function(e,t,n){"use strict";n("./node_modules/react/index.js");var o,i=n("./bundled-modules/styled-components/styled-components.min.js"),r=n.n(i),s=n("./src/reddit/components/Widgets/ThemedWidget/index.tsx"),d=n("./src/reddit/helpers/styles/mixins/fonts.tsx"),a=(o="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103,function(e,t,n,i){var r=e&&e.defaultProps,s=arguments.length-3;if(t||0===s||(t={}),t&&r)for(var d in r)void 0===t[d]&&(t[d]=r[d]);else t||(t=r||{});if(1===s)t.children=i;else if(s>1){for(var a=Array(s),c=0;c<s;c++)a[c]=arguments[c+3];t.children=a}return{$$typeof:o,type:e,key:void 0===n?null:""+n,ref:null,props:t,_owner:null}});const c=r.a.div.withConfig({componentId:"s21l9wz-0"})(["flex: 0 0 33.333%;width: 33.333%;"]);var l=r()(e=>a("div",{className:e.className},void 0,a(c,{},void 0,e.children[0]),a(c,{},void 0,e.children[1]),a(c,{},void 0,e.children[2]))).withConfig({componentId:"s21l9wz-1"})(["display: flex;flex-direction: row;"]),p=n("./src/app/strings/index.ts"),u=function(){var e="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103;return function(t,n,o,i){var r=t&&t.defaultProps,s=arguments.length-3;if(n||0===s||(n={}),n&&r)for(var d in r)void 0===n[d]&&(n[d]=r[d]);else n||(n=r||{});if(1===s)n.children=i;else if(s>1){for(var a=Array(s),c=0;c<s;c++)a[c]=arguments[c+3];n.children=a}return{$$typeof:e,type:t,key:void 0===o?null:""+o,ref:null,props:n,_owner:null}}}();const g=r()(l).withConfig({componentId:"s1168hkq-0"})(["margin-bottom: 16px;padding: 12px;"]),m=r.a.a.withConfig({componentId:"s1168hkq-1"})(["","display: block;text-decoration: none;text-transform: capitalize;"],d.titleFontH6),b=r.a.div.withConfig({componentId:"s1168hkq-2"})(["","text-align: center;padding-bottom: 12px;"],d.titleFontH6),f=r.a.a.withConfig({componentId:"s1168hkq-3"})(["text-decoration: none;text-transform: capitalize;margin: 0 4px;"]),h=r()(s.a).withConfig({componentId:"s1168hkq-4"})(["margin-top: ",";"],e=>e.removePaddingTop?0:"16px");t.a=(e=>u(h,{redditStyle:e.redditStyle,contentOnly:!0,removePaddingTop:e.removePaddingTop},void 0,u(g,{},void 0,u("div",{},void 0,u(m,{href:"https://about.reddit.com"},void 0,Object(p.a)("en","footer.links.about")),u(m,{href:"https://about.reddit.com/careers/"},void 0,Object(p.a)("en","footer.links.careers")),u(m,{href:"https://about.reddit.com/press/"},void 0,Object(p.a)("en","footer.links.press"))),u("div",{},void 0,u(m,{href:"https://about.reddit.com/advertise/"},void 0,Object(p.a)("en","footer.links.ad")),u(m,{href:"http://www.redditblog.com/"},void 0,Object(p.a)("en","footer.links.blog")),u(m,{href:"https://www.reddithelp.com"},void 0,Object(p.a)("en","footer.links.help"))),u("div",{},void 0,u(m,{href:"https://www.reddit.com/mobile/download"},void 0,Object(p.a)("en","footer.links.app")),u(m,{href:"https://www.reddit.com/coins"},void 0,Object(p.a)("en","footer.links.coins")),u(m,{href:"https://www.reddit.com/premium"},void 0,Object(p.a)("en","footer.links.premium")),u(m,{href:"http://redditgifts.com/"},void 0,Object(p.a)("en","footer.links.gifts")))),u(b,{},void 0,u("div",{},void 0,u(f,{href:"https://www.reddit.com/help/contentpolicy"},void 0," ",Object(p.a)("en","footer.legal.content")),u("span",{},void 0,"|"),u(f,{href:"https://www.reddit.com/help/privacypolicy"},void 0," ",Object(p.a)("en","footer.legal.privacy"))),u("div",{},void 0,u(f,{href:"https://www.reddit.com/help/useragreement"},void 0," ",Object(p.a)("en","footer.legal.user")),u("span",{},void 0,"|"),u(f,{href:"https://www.reddit.com/help/healthycommunities/"},void 0," ",Object(p.a)("en","footer.legal.mod"))),u("div",{},void 0,Object(p.a)("en","footer.legal.cp")))))},"./src/reddit/components/SidebarSectionHeader/index.tsx":function(e,t,n){"use strict";n.d(t,"b",function(){return s});var o=n("./src/reddit/models/Theme/NewColorSystem/index.ts"),i=n("./bundled-modules/styled-components/styled-components.min.js"),r=n.n(i);const s=`\n  ${n("./src/reddit/helpers/styles/mixins/fonts.tsx").labelsFont}\n  padding-bottom: 4px;\n`;t.a=r.a.div.withConfig({componentId:"s12kkcqc-0"})(["","border-bottom: 2px solid ",";color: ",";margin-bottom: 10px;"],s,e=>Object(o.c)(e).field,e=>Object(o.c)(e).actionIcon)},"./src/reddit/components/SidebarSpacer/index.tsx":function(e,t,n){"use strict";var o=n("./bundled-modules/styled-components/styled-components.min.js"),i=n.n(o),r=n("./src/reddit/constants/componentSizes.ts");t.a=i.a.div.withConfig({componentId:"ii4q9d-0"})(["margin-top: 16px;width: ","px;"],r.D)},"./src/reddit/components/Widgets/Base/index.tsx":function(e,t,n){"use strict";n.d(t,"b",function(){return c}),n.d(t,"a",function(){return p});n("./node_modules/react/index.js");var o,i=n("./src/reddit/components/SidebarSectionHeader/index.tsx"),r=n("./src/reddit/models/Theme/NewColorSystem/index.ts"),s=n("./bundled-modules/styled-components/styled-components.min.js"),d=n.n(s),a=(o="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103,function(e,t,n,i){var r=e&&e.defaultProps,s=arguments.length-3;if(t||0===s||(t={}),t&&r)for(var d in r)void 0===t[d]&&(t[d]=r[d]);else t||(t=r||{});if(1===s)t.children=i;else if(s>1){for(var a=Array(s),c=0;c<s;c++)a[c]=arguments[c+3];t.children=a}return{$$typeof:o,type:e,key:void 0===n?null:""+n,ref:null,props:t,_owner:null}});const c="\n  \n  border-radius: 5px 5px 4px 4px;\n  overflow: visible;\n  word-wrap: break-word;\n",l=d.a.div.withConfig({componentId:"s1npjf9r-0"})(["","background-color: ",";padding: 12px;"],c,e=>Object(r.c)(e).body),p=d.a.h3.withConfig({componentId:"s1npjf9r-1"})(["","color: ",";"],i.b,e=>Object(r.c)(e).navIcon);t.c=(e=>a("div",{className:e.className},void 0,a(l,{},void 0,e.children)))},"./src/reddit/components/Widgets/ThemedWidget/index.m.less":function(e,t,n){e.exports={widgetHeader:"_ZhON3a3vplThB8NFwuJn",widgetTitle:"_2sggAEfRQLyoAl4J__5twU",widgetContent:"TmgZY6tDcdErbE5d7E0HJ",widgetContentOnly:"_3RPJ8hHnfFohktLZca18J6"}},"./src/reddit/components/Widgets/ThemedWidget/index.tsx":function(e,t,n){"use strict";var o=n("./node_modules/polished/dist/polished.es.js"),i=n("./node_modules/react/index.js"),r=n.n(i),s=n("./node_modules/react-redux/es/index.js"),d=n("./node_modules/reselect/lib/index.js"),a=n("./bundled-modules/styled-components/styled-components.min.js"),c=n.n(a),l=n("./src/reddit/components/Widgets/Base/index.tsx"),p=n("./src/reddit/helpers/styles/mixins/fonts.tsx"),u=n("./src/reddit/selectors/user.ts"),g=n("./src/reddit/models/NewStructuredStyles/index.ts"),m=n("./src/reddit/models/Theme/index.ts"),b=n("./src/reddit/models/Theme/NewColorSystem/index.ts");const f=e=>e.isNightmodeOn?g.b.widgetColors.sidebarWidgetBackgroundColor:e.redditStyle?g.a.widgetColors.sidebarWidgetBackgroundColor:e.styles&&e.styles.backgroundColor?e.styles.backgroundColor:Object(b.c)(e).widgetColors.sidebarWidgetBackgroundColor,h=e=>e.isNightmodeOn?g.b.widgetColors.sidebarWidgetHeaderColor:e.redditStyle?g.a.widgetColors.sidebarWidgetHeaderColor:e.styles&&e.styles.headerColor?e.styles.headerColor:Object(b.c)(e).widgetColors.sidebarWidgetHeaderColor,y=e=>{if(e.isNightmodeOn)return g.b.bodyText;const t=f(e);return Object(m.f)(t)},x=e=>{if(e.isNightmodeOn)return g.b.metaText;const t=h(e);return Object(m.f)(t)};var v,w=n("./src/reddit/components/Widgets/ThemedWidget/index.m.less"),O=n.n(w),j=(v="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103,function(e,t,n,o){var i=e&&e.defaultProps,r=arguments.length-3;if(t||0===r||(t={}),t&&i)for(var s in i)void 0===t[s]&&(t[s]=i[s]);else t||(t=i||{});if(1===r)t.children=o;else if(r>1){for(var d=Array(r),a=0;a<r;a++)d[a]=arguments[a+3];t.children=d}return{$$typeof:v,type:e,key:void 0===n?null:""+n,ref:null,props:t,_owner:null}});const C=Object(s.connect)(()=>Object(d.createStructuredSelector)({isNightmodeOn:u.L})),I=c()(e=>r.a.createElement("div",e)).withConfig({componentId:"izgy8a-0"})(["","background-color: ",";color: ",";fill: ",";",";."," {",";background-color: ",";color: ",";fill: ",";button, a {&:hover {background-color: ",";}}}"],l.b,e=>f(e),e=>y(e),e=>y(e),e=>e.onClick?"cursor: pointer":"",O.a.widgetHeader,p.labelsFont,e=>h(e),e=>x(e),e=>x(e),e=>Object(o.e)(x(e),.2));t.a=C(e=>j(I,{className:e.className,"data-redditstyle":e.redditStyle,redditStyle:e.redditStyle,isNightmodeOn:e.isNightmodeOn,onClick:e.onClick,styles:e.styles},void 0,e.title&&j("div",{className:O.a.widgetHeader},void 0,j("div",{className:O.a.widgetTitle},void 0,e.title),e.headerButton),j("div",{className:e.contentOnly?O.a.widgetContentOnly:O.a.widgetContent},void 0,e.children)))},"./src/reddit/helpers/trackers/modHub.ts":function(e,t,n){"use strict";n.d(t,"b",function(){return r}),n.d(t,"c",function(){return s}),n.d(t,"a",function(){return d});var o=n("./src/reddit/selectors/telemetry.ts");const i=e=>({screen:o.screen(e),subreddit:o.subreddit(e),userSubreddit:o.userSubreddit(e)}),r=e=>t=>Object.assign({source:"mod_hub_nav",action:"click",noun:e},i(t)),s=()=>e=>Object.assign({source:"breadcrumb",action:"click",noun:"subreddit"},i(e)),d=()=>e=>Object.assign({source:"id_card",action:"click",noun:"mod_hub_nav"},i(e))},"./src/reddit/layout/threeCol/ExpandCenter/index.tsx":function(e,t,n){"use strict";n("./node_modules/react/index.js");var o,i=n("./bundled-modules/styled-components/styled-components.min.js"),r=n.n(i),s=n("./src/higherOrderComponents/warnOnChildrenCount/index.tsx"),d=n("./src/reddit/helpers/styles/components/index.tsx"),a=(o="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103,function(e,t,n,i){var r=e&&e.defaultProps,s=arguments.length-3;if(t||0===s||(t={}),t&&r)for(var d in r)void 0===t[d]&&(t[d]=r[d]);else t||(t=r||{});if(1===s)t.children=i;else if(s>1){for(var a=Array(s),c=0;c<s;c++)a[c]=arguments[c+3];t.children=a}return{$$typeof:o,type:e,key:void 0===n?null:""+n,ref:null,props:t,_owner:null}});const c=r()(Object(d.a)()).withConfig({componentId:"s1akftvf-0"})(["flex: 0 0 ",";"],e=>e.width?`${e.width}px`:""),l=r.a.div.withConfig({componentId:"s1akftvf-1"})(["flex: 1 1 100%;width: 100%;"]),p=r()(Object(d.a)()).withConfig({componentId:"s1akftvf-2"})(["flex: 0 0 ",";"],e=>e.width?`${e.width}px`:"");t.a=r()(Object(s.a)(e=>a("div",{className:e.className},void 0,a(c,{width:e.widthLeft},void 0,Array.isArray(e.children)&&e.children[0]),a(l,{},void 0,Array.isArray(e.children)&&e.children[1]),a(p,{width:e.widthRight},void 0,Array.isArray(e.children)&&e.children[2])),3)).withConfig({componentId:"s1akftvf-3"})(["display: flex;flex-direction: row;"])},"./src/reddit/selectors/widgets.ts":function(e,t,n){"use strict";n.d(t,"a",function(){return c}),n.d(t,"j",function(){return l}),n.d(t,"c",function(){return p}),n.d(t,"h",function(){return u}),n.d(t,"d",function(){return g}),n.d(t,"e",function(){return m}),n.d(t,"i",function(){return b}),n.d(t,"g",function(){return f}),n.d(t,"f",function(){return h}),n.d(t,"b",function(){return y});var o=n("./src/lib/objectSelector/index.ts"),i=n("./src/reddit/constants/posts.ts"),r=n("./src/reddit/helpers/name/index.ts"),s=n("./src/reddit/models/Widgets/index.ts"),d=n("./src/reddit/selectors/profile.ts"),a=n("./src/reddit/selectors/subreddit.ts");const c=e=>e.widgets.models,l=Object(o.a)((e,t)=>Object(s.p)(t)?e.widgets.models[t.widgetId]:Object(s.j)(t.widgetKind)),p=(e,t)=>{let n=t.subredditId;if(!n&&t.subredditName&&(n=Object(a.z)(e,t.subredditName)),n){const t=((e,t)=>e.widgets.idCardIds[t.subredditId])(e,{subredditId:n});if(t)return e.widgets.models[t]}return null},u=(e,t)=>e.widgets.sidebar[t.subredditId]||[],g=(e,t)=>e.widgets.menuIds[t.subredditId],m=(e,t)=>{const n=g(e,t);return n?e.widgets.models[n]:null},b=(e,t)=>{return e.widgets.sidebar[t.subredditId].reduce((t,n)=>{const o=e.widgets.models[n];return o&&t.push(o.kind),t},[])},f=(e,t)=>{const n=u(e,t);for(const o of n){const t=e.widgets.models[o];if("subreddit-rules"===t.kind)return t}return null},h=(e,t)=>{const n=u(e,t).map(t=>e.widgets.models[t]).filter(e=>"post-flair"===e.kind);return n.length?n:null},y=Object(o.a)((e,t)=>{if(t.type===i.a.PROFILE){const n=Object(d.g)(e,{profileName:t.name});return n?{profile:{id:n.id,name:Object(r.f)(n.name)}}:{}}const n=Object(a.w)(e,{subredditName:t.name});return{subreddit:{categoryName:Object(a.t)(e,{subredditName:t.name}).contentCategory,id:n.id,name:Object(r.f)(n.name)}}})}}]);
//# sourceMappingURL=CollectionCommentsPage~CommentsPage~Frontpage~PostCreation~PostDraft~SearchResults~Subreddit.9a383988057a711fd102.js.map
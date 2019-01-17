(window.webpackJsonp=window.webpackJsonp||[]).push([["CollectionCommentsPage~CommentsPage~Frontpage~ModListing~ModQueuePages~ModerationPages~Multireddit~N~e8353e1a"],{"./src/app/helpers/describeApiError/index.ts":function(e,n,o){"use strict";o.d(n,"a",function(){return i});var t=o("./src/app/strings/index.ts"),r=o("./src/lib/constants/index.ts");function i({apiError:e,isLoggedOut:n,language:o}){switch(e.type){case r.I.AUTHORIZATION_ERROR:return n?Object(t.a)(o,"error.type.notLoggedIn"):Object(t.a)(o,"error.type.notAuthorized");case r.I.VALIDATION_ERROR:return Object(t.a)(o,"error.type.validation");case r.I.NOT_FOUND_ERROR:return Object(t.a)(o,"error.type.notFound");case r.I.SERVER_ERROR:return Object(t.a)(o,"error.type.server");case r.I.LIKELY_UBLOCK_ERROR:return Object(t.a)(o,"error.type.blocked");default:return Object(t.a)(o,"error.type.generic")}}},"./src/lib/intersectionObserver/index.ts":function(e,n,o){"use strict";let t;o.d(n,"a",function(){return a}),o.d(n,"b",function(){return s});const r=new Map,i=new Map;"undefined"!=typeof window&&(o("./node_modules/intersection-observer/intersection-observer.js"),t=new IntersectionObserver(e=>{e.forEach(e=>{const n=e.target,o=e.intersectionRatio>0;if(o!==!!i.get(n)){i.set(n,o);const t=r.get(n);if(t){t(e,o&&!!i.get(n))}}})},{threshold:[.001]}));const a=(e,n)=>{try{r.set(e,n),t&&t.observe(e)}catch(o){0}},s=e=>{try{r.delete(e),t&&t.unobserve(e)}catch(n){0}}},"./src/lib/opener/index.ts":function(e,n,o){"use strict";o.d(n,"a",function(){return t});const t={SELF:"_self",BLANK:"_blank",PARENT:"_parent",TOP:"_top"};n.b=((e,n=t.SELF,o)=>{if(n===t.BLANK){const t=window.open("",n,o);null!=t?(t.opener=null,t.location.href=e):window.location.href=e}else window.location.href=e})},"./src/reddit/components/PromoBanners/index.tsx":function(e,n,o){"use strict";var t,r=o("./node_modules/history/index.js"),i=o("./node_modules/react/index.js"),a=o.n(i),s=o("./node_modules/react-redux/es/index.js"),d=o("./node_modules/reselect/lib/index.js"),l=o("./src/lib/cache/index.ts"),c=o("./src/lib/localStorageAvailable/index.ts"),p=o("./src/lib/loginHref/index.ts"),g=o("./src/reddit/actions/login.ts"),m=o("./src/reddit/actions/modal.ts"),u=o("./src/reddit/actions/promo.ts"),b=o("./src/config.ts"),h=o("./bundled-modules/styled-components/styled-components.min.js"),f=o.n(h),x=o("./src/app/strings/index.ts"),v=o("./src/lib/colors/constants.ts"),y=o("./src/lib/prettyPrintNumber/index.ts"),w=o("./src/reddit/constants/promos.ts"),j=o("./src/reddit/controls/Button/index.tsx"),O=o("./src/reddit/helpers/styles/mixins/fonts.tsx"),B=o("./src/reddit/icons/svgs/Close/index.tsx"),P=(t="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103,function(e,n,o,r){var i=e&&e.defaultProps,a=arguments.length-3;if(n||0===a||(n={}),n&&i)for(var s in i)void 0===n[s]&&(n[s]=i[s]);else n||(n=i||{});if(1===a)n.children=r;else if(a>1){for(var d=Array(a),l=0;l<a;l++)d[l]=arguments[l+3];n.children=d}return{$$typeof:t,type:e,key:void 0===o?null:""+o,ref:null,props:n,_owner:null}});const k=f.a.h1.withConfig({componentId:"s1r1dynj-0"})(["","color: ",";font-size: 32px;font-weight: bold;"],O.titleFontH1,v.n),C=f()(k).withConfig({componentId:"s1r1dynj-1"})(["","","line-height: initial;margin-right: 16px;"],O.titleFontH2,""),I=f.a.span.withConfig({componentId:"s1r1dynj-2"})(["","color: ",";display: block;padding-top: 4px;"],O.bodyFontH6,v.n),S=f()(j.e).withConfig({componentId:"s1r1dynj-3"})(["background-color: ",";border-color: ",";color: ",";display: inline-block;margin: 8px 0 0 0;max-height: 32px;white-space: nowrap;&:hover {background-color: ",";border-color: ",";color: ",";}"],v.e,v.e,v.n,v.d,v.d,v.n),L=Object(h.css)(["background-color: rgb(3, 46, 94);background-position: right;background-repeat: no-repeat;background-size: contain;border-radius: 4px;position: relative;"]),E=f()(e=>P("div",{className:e.className},void 0,e.children)).withConfig({componentId:"s1r1dynj-4"})(["","margin-bottom: 8px;padding: 16px;",""],L,e=>e.largeBannerKey===w.k.join?`background-image: url(${b.a.assetPath}/img/banner/banner-${w.k.welcome}@2x.png);`:`background-image: url(${b.a.assetPath}/img/banner/banner-${e.largeBannerKey}@2x.png);`),M=f.a.div.withConfig({componentId:"s1r1dynj-5"})(["","align-items: center;background-image: url(","/img/banner/banner-small@2x.png);background-position: left;display: flex;margin-bottom: 8px;padding: 16px 32px 16px 8px;"," {margin: 0 0 0 auto;}"],L,b.a.assetPath,S),N=f.a.div.withConfig({componentId:"s1r1dynj-6"})(["align-items: center;display: flex;flex-wrap: wrap;min-height: 42px;"," {margin: 0;}"," {margin-right: 20px;margin-left: 0px;}"],S,C),U=f.a.img.withConfig({componentId:"s1r1dynj-7"})(["margin: 0 8px;"]),R=f()(e=>P("button",{className:e.className,onClick:e.onClick},void 0,P(B.a,{}))).withConfig({componentId:"s1r1dynj-8"})(["height: 12px;width: 12px;right: 10px;top: 10px;position: absolute;svg {fill: ",";}"],v.n),$=e=>P(E,{largeBannerKey:e.largeBannerKey},void 0,P(R,{onClick:()=>e.closeBanner(w.h.UpsellSignUpBannerLarge,w.g[e.largeBannerKey])}),P(k,{},void 0,Object(x.a)(e.language,`promoBanners.${e.largeBannerKey}.header`)),P(I,{},void 0,Object(x.a)(e.language,`promoBanners.${e.largeBannerKey}.subHeader`)),P(S,{href:e.href,onClick:n=>{n.stopPropagation(),n.preventDefault(),e.onOpenRegisterModal(w.g[e.largeBannerKey])}},void 0,Object(x.a)(e.language,`promoBanners.${e.largeBannerKey}.button`))),T=e=>P(M,{},void 0,P(R,{onClick:()=>e.closeBanner(w.h.UpsellSignUpBannerMedium,w.g.join)}),P(U,{srcSet:`${b.a.assetPath}/img/banner/banner-small-logo.png 1x,\n        ${b.a.assetPath}/img/banner/banner-small-logo@2x.png 2x,`}),P(C,{},void 0,e.subreddit?Object(x.a)(e.language,"promoBanners.subreddit.header",{subredditName:e.subreddit.displayText,subscribers:Object(y.b)(e.subreddit.subscribers)}):Object(x.a)(e.language,"promoBanners.join.header")),P(S,{href:e.href,onClick:n=>{n.stopPropagation(),n.preventDefault(),e.onOpenRegisterModal(w.g.join)}},void 0,Object(x.a)(e.language,"promoBanners.personalize.button"))),D=f()(e=>P("div",{className:e.className},void 0,P(R,{onClick:()=>e.closeBanner(w.h.UpsellSignUpBannerSmall,w.g.join)}),P(N,{},void 0,P(U,{srcSet:`${b.a.assetPath}/img/banner/banner-small-logo.png 1x,\n          ${b.a.assetPath}/img/banner/banner-small-logo@2x.png 2x,`}),P(C,{},void 0,Object(x.a)(e.language,"promoBanners.join.header")),P(S,{href:e.href,onClick:n=>{n.stopPropagation(),n.preventDefault(),e.onOpenRegisterModal(w.g.join)}},void 0,Object(x.a)(e.language,"promoBanners.join.button"))))).withConfig({componentId:"s1r1dynj-9"})(["","background-image: url(","/img/banner/banner-small@2x.png);background-position: left;","padding: 4px 32px 4px 8px;"],L,b.a.assetPath,e=>e.isOverlay?"border-radius: 0;":"");var F=o("./src/reddit/actions/toaster.ts"),_=o("./src/reddit/helpers/trackers/banners.ts"),H=o("./src/reddit/components/TrackingHelper/index.tsx"),A=o("./src/lib/constants/index.ts"),K=o("./src/lib/makeRequest/index.ts");const X=(e,n)=>Object(K.b)({endpoint:"https://api.linktexting.com/sendLink",method:A.Ia.POST,data:`linkId=${n}&number=${e}`,headers:{Accept:"application/json","Content-Type":"application/x-www-form-urlencoded"}});var z=o("./src/reddit/models/Toast/index.ts"),V=function(){var e="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103;return function(n,o,t,r){var i=n&&n.defaultProps,a=arguments.length-3;if(o||0===a||(o={}),o&&i)for(var s in i)void 0===o[s]&&(o[s]=i[s]);else o||(o=i||{});if(1===a)o.children=r;else if(a>1){for(var d=Array(a),l=0;l<a;l++)d[l]=arguments[l+3];o.children=d}return{$$typeof:e,type:n,key:void 0===t?null:""+t,ref:null,props:o,_owner:null}}}();const q=f()(e=>V("button",{className:e.className,onClick:e.onCloseBanner},void 0,V(B.a,{}))).withConfig({componentId:"uob30s-0"})(["height: 12px;position: absolute;right: 10px;top: 10px;width: 12px;svg {fill: ",";}"],v.n),J=f()(j.d).withConfig({componentId:"uob30s-1"})(["width: 123px;height: 26px;line-height: 20px;background-color: ",";border-color: ",";color: ",";&:hover {background-color: ",";border-color: ",";color: ",";}"],v.e,v.e,v.n,v.e,v.e,v.n),Q=f.a.div.withConfig({componentId:"uob30s-2"})(["margin-bottom: 8px;"]),Y=f.a.div.withConfig({componentId:"uob30s-3"})(["background-color: rgb(3, 46, 94);background-position: right;background-repeat: no-repeat;background-size: contain;border-radius: 4px;display: flex;flex-wrap: wrap;padding: 16px 16px 14px 16px;position: relative;@media (min-width: 550px) {background-image: url(","/img/banner/mobile-x-promo.png);}"],b.a.assetPath),Z=f()(e=>V("div",{className:e.className},void 0,e.children)).withConfig({componentId:"uob30s-4"})(["margin-top: 1px;height: 100%;overflow: hidden;transition: max-height 0.3s;background-color: ",";",""],e=>e.shouldDisplayLegalDropdown?`${v.e}`:"rgb(3, 46, 94)",e=>e.shouldDisplayLegalDropdown?`max-height: ${e.isHidden?"0":"58px"};`:"max-height: 58px;"),G=f()(e=>V("span",{className:e.className},void 0,e.children)).withConfig({componentId:"uob30s-5"})(["","color: ",";display: block;font-size: 10px;line-height: 12px;opacity: 0.8;padding: 5px 22px;text-align: ",";"],O.bodyFontH6,v.n,e=>e.shouldDisplayLegalDropdown?"center":"left"),W=f.a.h1.withConfig({componentId:"uob30s-6"})(["","color: ",";margin-bottom: 5px;"],O.titleFontH1,v.n),ee=f.a.div.withConfig({componentId:"uob30s-7"})(["display: flex;flex-wrap: wrap;"]),ne=f.a.div.withConfig({componentId:"uob30s-8"})(["margin-right: 8px;"]),oe=f.a.div.withConfig({componentId:"uob30s-9"})(["display: flex;align-items: center;margin-bottom: 5px;"]),te=f.a.img.withConfig({componentId:"uob30s-10"})(["height: 16px;width: 16px;margin-right: 8px;"]),re=f()(te).withConfig({componentId:"uob30s-11"})(["width: auto;height: 12px;"]),ie=f.a.span.withConfig({componentId:"uob30s-12"})(["","color: ",";"],O.bodyFontH6,v.n),ae=f.a.div.withConfig({componentId:"uob30s-13"})(["align-items: center;display: flex;margin-top: 11px;"]),se=f()(e=>a.a.createElement("input",e)).withConfig({componentId:"uob30s-14"})(["","border-radius: 4px;height: 24px;margin-right: 5px;padding-left: 5px;width: 162px;",""],O.bodyFontH6,e=>e.error?`border: 1px solid ${v.l}`:"border: 1px solid transparent"),de=f.a.span.withConfig({componentId:"uob30s-15"})(["color: ",";display: block;font-size: 10px;margin-top: 7px;margin-left: 6px;opacity: .9;"],v.n),le=f.a.div.withConfig({componentId:"uob30s-16"})(["margin-left: 20px;"]),ce=f.a.img.withConfig({componentId:"uob30s-17"})(["margin: 0 auto;display: block;margin-bottom: 5px;border-radius: 4px;padding: 3px;height: 75px;width: 75px;background-color: white;margin-bottom: 5px;"]),pe=f.a.span.withConfig({componentId:"uob30s-18"})(["","color: ",";max-width: 126px;display: block;text-align: center;text-transform: inherit;"],O.bodyFontH6,v.n);var ge=Object(s.connect)(void 0,(e,n)=>({displayErrorToast:n=>{e(Object(F.e)({kind:z.b.Error,text:n}))},displaySuccessToast:n=>{e(Object(F.e)({kind:z.b.SuccessCommunity,text:n}))}}))(Object(H.b)(class extends a.a.Component{constructor(e){super(e),this.getLinkId=(()=>this.props.loggedInMobilePromoVariant?w.a:w.b),this.onBlur=(e=>{const n=!!e.currentTarget.value.length;this.setState({isLegalDropdownHidden:!n})}),this.onFocus=(e=>{this.setState({isLegalDropdownHidden:!1})}),this.onInputChange=(e=>{this.setState({phoneNumber:e.target.value.replace(/\D/,"")})}),this.onSubmit=(async()=>{var e=this.props;const n=e.language,o=e.displayErrorToast,t=e.displaySuccessToast,r=e.sendEvent,i=Object(x.a)(n,"promoBanners.mobileXPromo.empty"),a=Object(x.a)(n,"promoBanners.mobileXPromo.error"),s=Object(x.a)(n,"promoBanners.mobileXPromo.success");if(!this.state.phoneNumber.length)return this.setState({inputError:!0}),void o(i);r(Object(_.d)("click",w.g.mobilePromoBanner));const d=this.getLinkId(),l=await X(this.state.phoneNumber,d);l&&l.ok?(this.setState({phoneNumber:"",inputError:!1}),t(s)):(this.setState({inputError:!0}),o(a))}),this.state={isLegalDropdownHidden:!0,phoneNumber:""}}render(){var e=this.props;const n=e.closeBanner,o=e.language,t=e.loggedInMobilePromoVariant,r=e.loggedOutMobilePromoVariant,i=t&&t===w.c.Test1,a=r&&r===w.d.Test1,s=!(!i&&!a);return V(Q,{},void 0,V(Y,{},void 0,V(q,{onCloseBanner:()=>n(w.h.MobilePromoBanner,w.g[w.h.MobilePromoBanner],w.j)}),V("div",{},void 0,V(W,{},void 0,Object(x.a)(o,"promoBanners.mobileXPromo.header")),V(ee,{},void 0,V(ne,{},void 0,V(oe,{},void 0,V(te,{src:`${b.a.assetPath}/img/banner/redditor@2x.png`}),V(ie,{},void 0,Object(x.a)(o,"promoBanners.mobileXPromo.manage"))),V(oe,{},void 0,V(te,{src:`${b.a.assetPath}/img/banner/subscribe@2x.png`}),V(ie,{},void 0,Object(x.a)(o,"promoBanners.mobileXPromo.subscriptions")))),V(ne,{},void 0,V(oe,{},void 0,V(te,{src:`${b.a.assetPath}/img/banner/download@2x.png`}),V(ie,{},void 0,Object(x.a)(o,"promoBanners.mobileXPromo.downloads"))),V(oe,{},void 0,V(re,{src:`${b.a.assetPath}/img/banner/rating@2x.png`}),V(ie,{},void 0,Object(x.a)(o,"promoBanners.mobileXPromo.rated"))))),V(ae,{},void 0,V(se,{type:"tel",onChange:this.onInputChange,placeholder:Object(x.a)(o,"promoBanners.mobileXPromo.placeholder"),error:this.state.inputError?1:0,onBlur:this.onBlur,onFocus:this.onFocus,value:this.state.phoneNumber}),V(J,{onClick:this.onSubmit},void 0,Object(x.a)(o,"promoBanners.mobileXPromo.button"))),V(de,{},void 0,Object(x.a)(o,"promoBanners.mobileXPromo.countryCode"))),V(le,{},void 0,V(ce,{src:this.props.loggedInMobilePromoVariant?`${b.a.assetPath}/img/banner/qr-code-logged-in.png`:`${b.a.assetPath}/img/banner/qr-code-logged-out.png`}),V(pe,{},void 0,Object(x.a)(o,"promoBanners.mobileXPromo.qr")))),V(Z,{isHidden:this.state.isLegalDropdownHidden,shouldDisplayLegalDropdown:s},void 0,V(G,{shouldDisplayLegalDropdown:s},void 0,Object(x.a)(o,"promoBanners.mobileXPromo.legal"))))}})),me=o("./src/reddit/contexts/PageLayer/index.tsx"),ue=o("./src/reddit/selectors/meta.ts");var be=o("./src/reddit/selectors/user.ts");const he=Object.keys(w.k),fe=he[Math.floor(Math.random()*Math.floor(he.length))],xe=Object(d.createStructuredSelector)({displayUpsellSignUpBannerLarge:e=>e.promos.upsellSignUpBannerLarge,displayUpsellSignUpBannerMedium:e=>e.promos.upsellSignUpBannerMedium,displayUpsellSignUpBannerSmall:e=>e.promos.upsellSignUpBannerSmall,language:be.J,isLoggedIn:be.D,displayMobilePromo:e=>e.promos.mobilePromoBanner,origin:ue.d,subreddit:me.q}),ve=Object(s.connect)(xe,(e,n)=>({closeBanner:(o,t,r)=>{e(Object(u.c)(o,r)),n.sendEvent(Object(_.d)("close",t))},displayBanner:(o,t)=>{e(Object(u.d)({promoType:o})),n.sendEvent(Object(_.d)("view",t))},onOpenRegisterModal:o=>{e(Object(m.m)({actionSource:m.a.PromoBanner})),e(Object(g.b)()),n.sendEvent(Object(_.d)("click",o))}})),ye=Object(me.t)({isFrontPage:me.y,pageLayer:e=>e,path:me.T});n.a=ye(Object(H.b)(ve(class extends i.Component{constructor(){super(...arguments),this.sendToRegister=((e,n)=>Object(p.a)(Object(r.createLocation)(e),n,"/register"))}componentDidMount(){var e=this.props;const n=e.displayBanner,o=e.isFrontPage,t=e.isLoggedIn,r=e.location,i=Object(c.a)(),a=!!Object(l.b)(w.i);if(i)switch(r){case w.f.FrontPage:return void(t||a||n(w.h.UpsellSignUpBannerLarge,w.g[fe]));case w.f.SubredditPage:return void(o||t||a||n(w.h.UpsellSignUpBannerMedium,w.g.join));case w.f.CommentsPage:t||a||n(w.h.UpsellSignUpBannerSmall,w.g.join)}}render(){var e=this.props;const n=e.closeBanner,o=e.displayMobilePromo,t=e.displayUpsellSignUpBannerLarge,r=e.displayUpsellSignUpBannerMedium,i=e.displayUpsellSignUpBannerSmall,s=e.isFrontPage,d=e.isLoggedIn,l=e.isOverlay,c=e.language,p=e.location,g=e.path,m=e.subreddit,u=e.onOpenRegisterModal,b=e.origin,h={closeBanner:n,href:this.sendToRegister(g,b),isOverlay:l,language:c,onOpenRegisterModal:u,subreddit:m},f=Object.assign({},h,{largeBannerKey:fe}),x=Object.assign({},h);if(m&&m.isQuarantined)return null;switch(p){case w.f.FrontPage:if(s){if(o)return a.a.createElement(ge,x);if(t)return a.a.createElement($,f)}break;case w.f.SubredditPage:if(!s&&!d&&r)return a.a.createElement(T,h);break;case w.f.CommentsPage:if(!d&&i)return a.a.createElement(D,h)}return null}})))},"./src/reddit/controls/MetaData/index.tsx":function(e,n,o){"use strict";o.d(n,"a",function(){return p}),o.d(n,"b",function(){return g}),o.d(n,"d",function(){return u}),o.d(n,"c",function(){return b});o("./node_modules/react/index.js");var t,r=o("./bundled-modules/styled-components/styled-components.min.js"),i=o.n(r),a=o("./src/app/strings/index.ts"),s=o("./src/lib/prettyPrintNumber/index.ts"),d=o("./src/reddit/helpers/styles/mixins/fonts.tsx"),l=o("./src/reddit/models/Theme/NewColorSystem/index.ts"),c=(t="function"==typeof Symbol&&Symbol.for&&Symbol.for("react.element")||60103,function(e,n,o,r){var i=e&&e.defaultProps,a=arguments.length-3;if(n||0===a||(n={}),n&&i)for(var s in i)void 0===n[s]&&(n[s]=i[s]);else n||(n=i||{});if(1===a)n.children=r;else if(a>1){for(var d=Array(a),l=0;l<a;l++)d[l]=arguments[l+3];n.children=d}return{$$typeof:t,type:e,key:void 0===o?null:""+o,ref:null,props:n,_owner:null}});const p=i.a.span.withConfig({componentId:"h5svje-0"})(["","color: ",";"],d.metadataFont,e=>Object(l.c)(e).metaText),g=()=>c(p,{},void 0," · "),m=Object(a.e)("comment.point"),u=(e,n,o)=>{const t=n?Object(a.a)(o,"comment.hiddenScorePlain"):m(o,e,{count:Object(s.b)(e)});return c(p,{},void 0,t)},b=(e,n)=>{const o=Object(a.d)(n,"posts.comments.noun",e,{count:Object(s.b)(e)});return c(p,{},void 0,o)}},"./src/reddit/helpers/trackers/banners.ts":function(e,n,o){"use strict";o.d(n,"d",function(){return t}),o.d(n,"c",function(){return r}),o.d(n,"b",function(){return i}),o.d(n,"a",function(){return a});const t=(e,n)=>o=>({source:"banner",action:e,noun:n}),r=e=>n=>({source:"announcement",noun:"announcement",action:"view",liveThread:{id:e,isAnnouncement:!0}}),i=e=>n=>({source:"announcement",noun:"announcement",action:"dismiss",liveThread:{id:e,isAnnouncement:!0}}),a=e=>n=>({source:"announcement",noun:"announcement",action:"click",liveThread:{id:e,isAnnouncement:!0}})}}]);
//# sourceMappingURL=CollectionCommentsPage~CommentsPage~Frontpage~ModListing~ModQueuePages~ModerationPages~Multireddit~N~e8353e1a.1171fa192800a2af10c6.js.map
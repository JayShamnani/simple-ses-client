if(!self.define){let e,s={};const i=(i,l)=>(i=new URL(i+".js",l).href,s[i]||new Promise((s=>{if("document"in self){const e=document.createElement("script");e.src=i,e.onload=s,document.head.appendChild(e)}else e=i,importScripts(i),s()})).then((()=>{let e=s[i];if(!e)throw new Error(`Module ${i} didn’t register its module`);return e})));self.define=(l,n)=>{const t=e||("document"in self?document.currentScript.src:"")||location.href;if(s[t])return;let r={};const c=e=>i(e,t),o={module:{uri:t},exports:r,require:c};s[t]=Promise.all(l.map((e=>o[e]||c(e)))).then((e=>(n(...e),r)))}}define(["./workbox-06bfb1fd"],(function(e){"use strict";e.setCacheNameDetails({prefix:"simple-mail-client"}),self.addEventListener("message",(e=>{e.data&&"SKIP_WAITING"===e.data.type&&self.skipWaiting()})),e.precacheAndRoute([{url:"/simple-ses-client/css/app.4520227b.css",revision:null},{url:"/simple-ses-client/img/logo.627c7dbf.png",revision:null},{url:"/simple-ses-client/index.html",revision:"2456b137cb50f9934c9c09e5873fc276"},{url:"/simple-ses-client/js/about.88a83630.js",revision:null},{url:"/simple-ses-client/js/app.f9e391df.js",revision:null},{url:"/simple-ses-client/js/chunk-vendors.dc788f15.js",revision:null},{url:"/simple-ses-client/manifest.json",revision:"df627ca575b2c6e9fa5edea27d843b15"},{url:"/simple-ses-client/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"}],{})}));
//# sourceMappingURL=service-worker.js.map

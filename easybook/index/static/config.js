/*! 2015 Baidu Inc. All Rights Reserved */
define("common/js/config",[],function(require){return{subKey:function(e){var t=e.indexOf("=");if(-1==t)return null;else return e.substring(0,t)},subTitle:function(e,t){var n;if(e.length>t)n=e.substring(0,t)+"...";else n=e;return n},urlHashJson:function(){var e=window.location.href,t={},n=e.indexOf("?");if(n>=0){var i=e.substr(n+1);if(-1!=i.indexOf("&")){strs=i.split("&");for(var r=0;r<strs.length;r++)t[strs[r].split("=")[0]]=strs[r].split("=")[1]}else t[i.split("=")[0]]=i.split("=")[1]}return t},locationHash:function(e){var t=window.location.toString(),n=t.substring(t.indexOf("?")+1,t.length);n=decodeURI(n),n=n.replace(/\s/g,"");for(var i=n.split("&"),r=0;r<i.length;r++)if(this.subKey(i[r])==e){var a=i[r].substring(i[r].indexOf("=")+1,i[r].length);return a}else return null},lsItem:function(e,t){var n=null;if(window.localStorage)if(t)localStorage.setItem(e,t),n=t;else n=localStorage.getItem(e);else alert("This browser does not support localStorage!");return n},lsRemoveItem:function(e){if(window.localStorage)localStorage.removeItem(e);else return alert("This browser does not support localStorage!"),!1;return!0},lsRemoveItems:function(){for(var e=arguments,t=0;t<e.length;t++)this.lsRemoveItem(e[t])},unLoad:function(){var e={};e.set=function(e){window.onbeforeunload=function(t){return t=t||window.event,t.returnValue=e,e}},e.clear=function(){fckDraft.delDraftById(),window.onbeforeunload=function(){}},this.lsRemoveItems("tempProvId","tempCityId","tempRegionId","tempLevel1Id","tempLevel2Id","tempMedTitle")},barCode:function(){var e=$(".bar-code");window.onscroll=window.onresize=function(){var t=e.height(),n=document.documentElement.clientHeight||document.body.clientHeight,i=document.documentElement.scrollTop||document.body.scrollTop,r=document.documentElement.scrollHeight||document.body.scrollHeight,a=n+i,o=r-a;if(t>o)e.css("bottom",t-o+"px"),console.log("offsetBarHeight:"+o);if(a==r)console.log("slideHeight:"+a),console.log("allHeight:"+r),e.css("bottom","100px");else console.log("slideHeight2:"+a),console.log("allHeight2:"+r),e.css("bottom","0px")}},keyParamer:function(e){var t="";for(var n in e)t+='<input type="hidden" name="'+n+'" value="'+e[n]+'" />';t+='<input type="hidden" name="searchTag" value="1" />',$('input[name="key"]')[0].value=$("input[name='key']")[0].value.replace(/(^\s*)|(\s*$)/g,""),$('input[name="key"]').after(t),$("#med_form").attr("action",""+this.api+"/pc/search/list").submit()},src:function(){var e=$(".footer-box").data("src");return e}(),href:function(){var e=$(".footer-box").data("href");return e}(),api:function(){var e=$(".footer-box").data("api");return e}(),keyWord:function(e){var t=this;$("#querySearch").on("click",function(n){var i=$("input[name='key']")[0].value.replace(/(^\s*)|(\s*$)/g,"");if(""!=i&&"请输入医院/科室/疾病/症状/医生姓名"!=i)return t.keyParamer(e),!1;else n.preventDefault?n.preventDefault():n.returnValue=!1,$("input[name='key']")[0].value=""}),$("#querySearch").on("keydown",function(n){var i=n.which;if(13==i){var r=$("input[name='key']")[0].value.replace(/(^\s*)|(\s*$)/g,"");if(""!=r&&"请输入医院/科室/疾病/症状/医生姓名"!=r)return t.keyParamer(e),!1;else n.preventDefault?n.preventDefault():n.returnValue=!1,$("input[name='key']")[0].value=""}}),$("input[name='key']").on("keydown",function(n){var i=n.which;if(13==i){var r=$("input[name='key']")[0].value.replace(/(^\s*)|(\s*$)/g,"");if(""!=r&&"请输入医院/科室/疾病/症状/医生姓名"!=r)return t.keyParamer(e),t.httpGet(1),!1;else n.preventDefault?n.preventDefault():n.returnValue=!1,$("input[name='key']")[0].value=""}})},init:function(){var e=$("#search-tips-input").attr("placeholder");if($("#search-tips-input").on("focus",function(){var t=$(this);if(this.value==e||""==t.val())this.value="",t.removeClass("gray")}),$("#search-tips-input").on("blur",function(){var t=$(this);if(""===this.value)this.value=e,t.addClass("gray")}),""===this.value)this.value=e;$(window).scroll(function(){if($(window).scrollTop()>0&&$(window).scrollTop()<=200)$("#button-top").show();else if(0==$(window).scrollTop())$("#button-top").hide()}),$("#button-top").find("img").mouseenter(function(){$(this).attr("src",$(this).data("srchover"))}),$("#button-top").find("img").mouseleave(function(){$(this).attr("src",$(this).data("src"))})}}});
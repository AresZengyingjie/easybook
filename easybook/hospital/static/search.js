/*! 2015 Baidu Inc. All Rights Reserved */
define("search/search",["require","common/js/ajax","common/js/pagination"],function(require){return{init:function(){},docSuccess:!1,hosSuccess:!1,reDocSuccess:!1,reHosSuccess:!1,httpGet:function(e,t,i,n,a,r,o,s){o=o||{},o.pageType=o.pageType||"";var l=this,c=require("common/js/ajax"),d=require("common/js/pagination"),u=$.extend({},t,l.getFilterData(a));c({url:""+l.api+e,type:"get",datatype:"json",data:u,success:function(c){if(c&&c.data){if("doctor"==i&&c.data.doctorList)if(1==$(".container").attr("data-accuracy"))n=$(".doctor-info-box"),l.viewAccurateDoctorList(c.data,n),r=$(".pagers");else l.viewDoctorList(c.data,n),l.pageEvent(),l.docSuccess=!0;else if("hospital"==i&&c.data.hospitalList)l.viewHospitalList(c.data,n,o),l.pageEvent(),l.hosSuccess=!0;else if("relativeDoc"==i&&c.data.doctorList)l.excelDoctorList=c.data.doctorList,l.viewExcelDoctor(s),l.excelDoctorDomEvent(s),l.reDocSuccess=!0;else if("relativeHos"==i&&c.data.hospitalList)l.relativeHos(c.data,n),l.reHosSuccess=!0;if(c.data.total)if("doctor"==i||"hospital"==i)new d({total:c.data.total,pageSize:10,curPage:a,pagerContainer:r,callback:function(a){l.httpGet(e,t,i,n,a,r,o)}}).init()}},error:function(e){}})},excelDoctorList:[],createExcelDoctorDom:function(e){var t=this;if(this.excelDoctorList&&e>this.excelDoctorList.length)return $('<li style="display:none;"></li>');var i=[];if(e%5==1)i.push('<li class="doctor-first">');else i.push("<li>");return e--,i.push('<a href="'+decodeURIComponent(t.excelDoctorList[e].link)+'" target="_blank"><img src="'+t.excelDoctorList[e].avatar+'"></a>'),i.push('<div class="doctor-opacity"><p class="skill">擅长:&nbsp;'+t.excelDoctorList[e].skillIndexCut+"</p></div>"),i.push('<p><a target="_blank" href="'+decodeURIComponent(t.excelDoctorList[e].link)+'" alt="'+t.excelDoctorList[e].wholeName+'" title="'+t.excelDoctorList[e].wholeName+'"><span>'+t.excelDoctorList[e].name+'</span></a>&nbsp;<span class="doctor-level">'+t.excelDoctorList[e].medTitle+"</span></p>"),i.push("<p>"+t.excelDoctorList[e].departName+"</p>"),i.push('<p title="'+t.excelDoctorList[e].hospitalName+'">'+t.excelDoctorList[e].hospitalNameCut+"</p>"),i.push('<p class="btn-appoint"><a target="_blank" href="'+decodeURIComponent(t.excelDoctorList[e].link)+'"><span>一键预约</span></a></p>'),i.push("</li>"),$(i.join("")).hover(function(){$(this).css("background-color","#f9f9f9"),$(this).find(".doctor-opacity").css("display","block"),$(this).find(".btn-appoint span").css({"background-color":"#0197f1","border-color":"#0197f1",color:"#fff"})},function(){$(this).css("background-color","#fff"),$(this).find(".doctor-opacity").css("display","none"),$(this).find(".btn-appoint span").css({"background-color":"#fbfbfb",color:"#333","border-color":"#e8e8e8"})})},viewExcelDoctor:function(e){if(this.excelDoctorList.length<=0)return void $("#excel-doctor-div").remove();else $("#excel-doctor-div").show();for(var t=$("#dictor-list-ul"),i=1;e>=i;i++){var n=this.createExcelDoctorDom(i);t.append(n)}},excelDoctorDomEvent:function(e){var t=this,i=1,n=$("#dictor-list-ul"),a=Math.floor(t.excelDoctorList.length/e)+(t.excelDoctorList.length%e>0);if(i!=a)$("#next-arrow").find("img").attr("src",$(this).data("src")),$("#pre-arrow").find("img").hover(function(){if(1!=i)$(this).css("cursor","pointer"),$(this).attr("src",$(this).data("srchover"))},function(){if(1!=i)$(this).attr("src",$(this).data("src"));else $(this).css("cursor","auto"),$(this).attr("src",$(this).data("gray"))}),$("#next-arrow").find("img").hover(function(){if(i!=a)$(this).css("cursor","pointer"),$(this).attr("src",$(this).data("srchover"))},function(){if(i!=a)$(this).attr("src",$(this).data("src"));else $(this).css("cursor","auto"),$(this).attr("src",$(this).data("gray"))}),$("#pre-arrow").click(function(){if(1==i)return!1;i--;for(var a=1;e>=a;a++)!function(e,i){setTimeout(function(){n.find("li:eq("+(e-1)+")").replaceWith(t.createExcelDoctorDom(5*(i-1)+e))},50*e)}(a,i);if(1==i)$("#pre-arrow").find("img").trigger("mouseleave")}),$("#next-arrow").click(function(){if(i==a)return!1;for(var r=e;r>=1;r--)!function(i,a){setTimeout(function(){n.find("li:eq("+(i-1)+")").replaceWith(t.createExcelDoctorDom(5*a+i))},50*(e-i))}(r,i);if(i++,i==a)$("#next-arrow").find("img").trigger("mouseleave")})},src:function(){var e=$(".footer-box").data("src");return e}(),href:function(){var e=$(".footer-box").data("href");return e}(),api:function(){var e=$(".footer-box").data("api");return e}(),createDoctorStr:function(e,t){for(var i=this,n=e.length,a=0;n>a;a++){if(t.push('<li class="doctor-info-single">'),t.push('<div class="doctor-card clearfix">'),t.push('<div class="info-pic"><a href="'+e[a].link+'" target="_blank" ><img src="'+e[a].avatar+'"></div>'),t.push('<div class="infos">'),t.push('<div class="info-title" style="margin-top:-10px\x00">'),t.push('<a href="'+e[a].link+'"  target="_blank" alt="'+e[a].wholeName+'" title="'+e[a].wholeName+'"><div>'+e[a].name+"</div></a>"),0!=e[a].isVerify)t.push('<a href="'+e[a].verifyLink+'" target="_blank"><i><img src="'+i.src+'/common/img/fill_icon_doctor-yi.png"/></i><span>百度认证医生</span></a>');if(t.push('<span class="doctor-medtitle">'+e[a].medTitle+"</span><span>"+e[a].eduTitle+"</span>"),t.push('<p class="info-hospittal"><span><a href="'+e[a].hospitalLink+'" target="_blank" >'+e[a].hospitalName+"</a></span>"+e[a].departName+"</p>"),t.push("<table cellSpacing=0 cellPadding=0>"),t.push('<tr class="doctor-good">'),t.push('<td class="first-td" valign="top">擅长诊治: </td>'),t.push('<td class="last-td" valign="top">'+e[a].skill+"</td>"),t.push("</tr>"),t.push("</table>"),t.push('<div class="rate">'),e[a].star>0){t.push("<span>总推荐度：</span>"),t.push('<div class="grade-star">');for(var r=.5;10>r;){if(e[a].star>r+1)t.push('<i class="star-right star-light star-fixed"></i>');else if(e[a].star>r)t.push('<i class="star-right star-gray-light star-fixed"></i>');else t.push('<i class="star-right star-gray star-fixed"></i>');r+=2}t.push("</div>")}t.push('<span>预约成功率：</span><i class="num">'+e[a].reservedRate+"</i>"),t.push("</div>"),t.push("</div>"),t.push("</div>"),t.push('<div class="appointment-time"><ul>');var o=e[a].appointTime.timeList;if(0==o.length)t.push("<li>已约满，每<em>半小时</em>更新号源，敬请关注。</li>");else for(var s=0;s<o.length;s++)t.push("<li>"),t.push('<span class="appointment-day">'+o[s].dateDesc+"</span>"),t.push("<span>"+o[s].date+"</span>"),t.push("<span>"+o[s].interval+"</span>"),t.push('<a href="'+o[s].buttonLink+'" target="_blank"><span class="appointment-click">'+o[s].buttonText+"</span></a>"),t.push("</li>");if(""!=e[a].appointTime.moreLink)t.push('<li><a href="'+e[a].appointTime.moreLink+'" class="more-time-chose" target="_blank"><span >更多时段&nbsp;></span></li></a>');t.push("</ul></div>"),t.push("</div>"),t.push("</li>")}},viewDoctorList:function(e,t){var i=this;$("#doc_total").html(e.total);var n=[],a=e.doctorList.length;if(0>=a)t.parents(".doctor-info-box").find(".pagination-x").hide(),t.hide(),$(".doctor-empty").show();else{$(".doctor-empty").hide(),t.show(),t.parents(".doctor-info-box").find(".pagination-x").show(),i.createDoctorStr(e.doctorList,n),t.html(n.join("")).show(),t.find(".doctor-info-single").last().css("border-bottom","1px solid #eaeaea !important"),t.find(".doctor-info-single").hover(function(){$(this).css("border","1px solid #60afff"),$(this).next().css("border-top","none")},function(){if($(this).css("border-top","1px solid #eaeaea"),$(this).css("border-right","1px solid #fff"),$(this).css("border-left","1px solid #fff"),$(this).css("border-bottom","none"),$(this).next().css("border-top","1px solid #eaeaea"),$(this).index()==t.find(".doctor-info-single").length-1)$(this).css("border-bottom","1px solid #eaeaea")});var r=parseInt(a/10);if(0==r)$("#doctor-info-list").find(".doctor-info-single").eq(-1).css("border-bottom-color","#fff")}},viewAccurateDoctorList:function(e,t){var i=this,n=e.doctorList.length?e.doctorList.length:0,a=[];if(e.accurateDoctorList&&e.accurateDoctorList.length>0)a.push('<h4>符合条件的 <font class="curdotor"><i id="total">'+e.total+"</i></font> 名优质医生</h4>"),a.push('<ul class="doctor-info-list">'),i.createDoctorStr(e.accurateDoctorList,a),a.push("</ul>");if(e.doctorList&&e.doctorList.length>0)a.push('<ul class="doctor-info-list" id="doctor-info-list">'),a.push('<h4 style="text-align: left;">为您推荐同科室的其他医生</h4>'),i.createDoctorStr(e.doctorList,a),a.push("</ul>");a.push('<div class="pagination-x pull-right">'),a.push('<span class="pagers"></span>'),a.push("</div>"),t.html(a.join(""));var r=parseInt(n/10);if(0==r)$("#doctor-info-list").find(".doctor-info-single").eq(-1).css("border-bottom-color","#fff")},viewHospitalList:function(e,t,i){var n=[];if($("#hos_total").html(e.total),e.currentArea)$("#hos_region").html(e.currentArea);else $("#hos_region").html("");var a=e.hospitalList?e.hospitalList.length:0;if(0>=a)t.hide(),t.parents(".hospital-list").find(".pagination-x").hide(),$(".hospital-empty").show();else{$(".hospital-empty").hide(),t.show(),t.parents(".hospital-list").find(".pagination-x").show();for(var r=0;a>r;r++){if(n.push('<li class="hospital-info-li">'),n.push('<div class="hospital-info">'),n.push('<div class="hospital-pic"><a href="'+e.hospitalList[r].link+'"><img src="'+e.hospitalList[r].logo+'"></a></div>'),n.push('<div class="hospital-introduces">'),n.push('<div class="introduces-title"><a href="'+e.hospitalList[r].link+'">'+e.hospitalList[r].name+"</a>"),e.hospitalList[r].level)n.push('<span class="hospital-sign">'+e.hospitalList[r].level+"</span>");if(1==e.hospitalList[r].insurance)n.push('<span class="hospital-health">医保</span>');if(n.push("</div>"),n.push("<table cellSpacing=0 cellPadding=0>"),n.push("<tr>"),n.push('<td valign="" class="first-child">医院地址: </td>'),n.push('<td class="info-pos last-child"><p class="address">'+e.hospitalList[r].address+'</p><a href="'+e.hospitalList[r].routeLink+'" class="marker" target="_blank"><i class="fa fa-map-marker"></i>查看地图</a>'),n.push("</td></tr>"),n.push('<tr class="last-child-tr">'),1==e.hospitalList[r].serviceGuahao||1==e.hospitalList[r].serviceTixing){if(n.push('<td valign="" class="first-child">提供服务: </td>'),n.push('<td valign="" class="server last-child">'),1==e.hospitalList[r].serviceGuahao&&1==e.hospitalList[r].serviceTixing)n.push("预约挂号&nbsp;/&nbsp;");else if(1==e.hospitalList[r].serviceGuahao)n.push("预约挂号");if(1==e.hospitalList[r].serviceTixing)n.push("就诊提醒");n.push("</td>")}else;n.push("</tr>"),n.push("</table>"),n.push("<label><span>"+e.hospitalList[r].doctorNum+"</span>位可挂号医生<span> | </span><span>"+e.hospitalList[r].serveNum+"</span>人预约成功</div></label>"),n.push("</div>"),n.push("</div>"),n.push("</li>")}t.html(n.join(""));var o=parseInt(a/10);if(0==o)$("#hospital-list-ul").find("li").eq(-1).css("border-color","#fff")}},pageEvent:function(){$(".pagination-x-list").find("li").length;$(".pagination-x-list").delegate("li","click",function(){if(0!==$(this).index()||$(this).index()!==$(".pagination-x-list").find("li").last().index())$("#fastTop").show()})},relativeHos:function(e){var t=this,i=[],n=e.hospitalList?e.hospitalList.length:0;if(!(0>=n)){$("#excel-hos-div").show();for(var a=0;n>a;a++){if(a%4==3)i.push('<li class="hospital-detail content-last">');else i.push('<li class="hospital-detail">');if(i.push('<a href="'+e.hospitalList[a].link+'" target="_blank"><img src="'+e.hospitalList[a].logo+'" width="230" height="120"></a>'),i.push('<p class="hospital-name">'),i.push('<a href="'+e.hospitalList[a].link+'" target="_blank" title="'+e.hospitalList[a].name+'" target="_blank"><span class="span-name">'+e.hospitalList[a].name+"</span></a>"),i.push('<label class="hospital-grade">'),e.hospitalList[a].level)i.push(' <span class="grade">'+e.hospitalList[a].level+"</span>");if(1==e.hospitalList[a].insurance)i.push('<span class="corpt">医保</span>');i.push("</label></p>"),i.push('<p class="appointent_total"><label class="label-left">'+e.hospitalList[a].doctorNum+'位可挂号医生</label><label class="label-right"><span>'+e.hospitalList[a].serveNum+"</span>人成功预约</label></p><li>")}$("#doctor_content").append(i.join(""))}else if($("#excel-hos-div").remove(),t.excelDoctorList.length<=0)$("#more-excel").remove()},areaEvent:function(){$(".city-index span").on("click",function(){$(".city-list div").hide().eq($(".city-index span").removeClass("border-bottom3px").addClass("border-bottom1px").index($(this).attr("class","border-bottom3px"))).show()}),$(".area-border").on("mouseenter",function(){$(this).find(".city-index").find("span").attr("class","border-bottom1px"),$(this).find(".city-list").find("div").hide();var e=$(this).find(".city-index").attr("data-index");$(this).find(".city-index").find("span").eq(e).attr("class","border-bottom3px"),$(this).find(".city-list").find("div").eq(e).show(),$(this).css("border-color","#eaeaea").find(".select-city").show()}).on("mouseleave",function(){$(this).css("border-color","#ffffff").find(".select-city").hide()})},getFilterData:function(e){var t={};if(t.page=e,paramdata=$("#header").data("paramdata"),paramdata)for(var i in paramdata)t[i]=paramdata[i];return t},backTop:function(){var e=$(".footer-box").height();$(window).scroll(function(){var t=$(this).scrollTop(),i=$(document).height(),n=$(this).height();if($(window).scrollTop()>30)$("#feedback").show();else if($(window).scrollTop()<30)$("#feedback").hide();var a=i-(t+n);if(e>=a)$("#feedback").css("bottom",e-a+15+"px");else $("#feedback").css("bottom","20px")}),$("#back-top").click(function(){return $("html,body").animate({scrollTop:"0px"},500),$(this).blur(),!1}),$("#back").click(function(){$(this).blur()}),$("#feedback").find("img").mouseenter(function(){$(this).attr("src",$(this).data("srchover"))}),$("#feedback").find("img").mouseleave(function(){$(this).attr("src",$(this).data("src"))})}}});
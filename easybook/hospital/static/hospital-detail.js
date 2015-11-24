/*! 2015 Baidu Inc. All Rights Reserved */
define("search/hospital-detail/hospital-detail",["search/search","hospital/id","common/js/ajax","common/js/pagination","common/js/mustache.min"],function(){var e=require("search/search"),t={};return t.init=function(){e.init();var t=$("#current-area");if(t.text().length>5)t.html(t.text().substr(0,4)+"...");this.select(),this.selectDash(),e.backTop(),$(".search_box").children(".area").children("div").css("display","block"),e.areaEvent(),this.orderTime(),this.lanchTab("#Tab"),this.initTab(),$(".hos-special-href").on("click",function(){var e="current";$("#Tab").find("a").eq(1).addClass(e).siblings().removeClass(e).end().index();$("#Tab").find(".content").eq(1).show().siblings().hide(),$("#tab-desc").click(),$(".doctor-empty").hide()}),e.httpGet("/pc/doctor/listdata",this.getFilterData(),"doctor",$("#doctor-info-list"),1,$(".pagers").eq(0))},t.api=function(){var e=$(".footer-box").data("api");return e}(),t.initTab=function(){var e=$("#Tab").find(".nav").find(".current").index();$(".nav a").eq(e).click()},t.lanchTab=function(e){var t=$(e),i="current";t.on("click",".hd",function(){var e=$(this).addClass(i).siblings().removeClass(i).end().index();t.find(".content").eq(e).show().siblings().hide()})},t.select=function(){var t=this;$(".select-condition").delegate("li","click",function(i){var n=i.target;t.searchTag=0;var a=$(n).attr("data-value"),r=$(n).parents(".select-detail").attr("data-type");if(1==r){$(n).parents(".select-detail").find("li").each(function(){$(this).removeClass("select-cur")});var o=0;if($(n).addClass("select-cur"),$("#second-depart").find("ul").each(function(){$(this).addClass("hide"),$("#second-depart").find("li").each(function(){$(this).removeClass("select-cur")})}),$("#second-depart").find("ul").each(function(){if(a==$(this).attr("data-value"))$(this).removeClass("hide"),$(this).children(":eq(0)").addClass("select-cur")}),$("#second-depart").find("ul").each(function(){if(!$(this).hasClass("hide"))o+=1}),0==o)$("#depart-level1-ul").css("margin-bottom","10px"),$("#second-depart").addClass("hide");else $("#depart-level1-ul").css("margin-bottom","0px"),$("#second-depart").removeClass("hide")}else $(n).parents(".select-detail").find("li").each(function(){$(this).removeClass("select-cur")}),$(n).addClass("select-cur");e.httpGet("/pc/doctor/listdata",t.getFilterData(),"doctor",$("#doctor-info-list"),1,$(".pagers").eq(0))})},t.selectDash=function(){if($(".select-condition").length>0){if($("#medtitle-ul").length>0&&0!=$(".select-condition").find("#medtitle-ul").parent().index())$("#medtitle-ul").parent().css("border-top","1px dashed #eaeaea");if($("#region").length>0&&0!=$(".select-condition").find("#region").index())$("#region").css({"border-top":"1px dashed #eaeaea","padding-bottom":"10px"})}},t.getFilterData=function(){var e={};return e.departmentFlag=$("#depart-level1-ul").find(".select-cur").data("departmentFlag")||0,e.hosId=require("hospital/id"),e.key=$("input[name='key']").attr("data-value"),e.date=$("#select-visit-time").find(".select-cur").attr("data-value"),e.departLevel1Id=$("#depart-level1-ul").find(".select-cur").attr("data-value"),e.departLevel2Id=$("#second-depart").find(".select-cur").attr("data-value"),e.medTitle=$("#medtitle-ul").find(".select-cur").attr("data-value"),e.pageSize=10,e.key="undefined"!=typeof e.key?e.key:"",e.date="undefined"!=typeof e.date?e.date:"",e.departLevel1Id="undefined"!=typeof e.departLevel1Id?e.departLevel1Id:"",e.departLevel2Id="undefined"!=typeof e.departLevel2Id?e.departLevel2Id:"",e.medTitle="undefined"!=typeof e.medTitle?e.medTitle:"",e},t.orderTime=function(){var t=this;$(".doctor-order-time").on("click",function(){$(".visit-hover").toggle()}),$(".doctor-visit-ul").delegate("li","click",function(i){var n=$(this);if(i.stopPropagation(),n.is(".date-group"))return i.preventDefault(),!0;if(n.is(".date-classify")||n.is(".date-unit")){$(".doctor-visit-ul").find("li").removeClass("select-cur");var a=$(i.currentTarget);a.addClass("select-cur"),$(".visit-hover").hide(),e.httpGet("/pc/doctor/listdata",t.getFilterData(),"doctor",$("#doctor-info-list"),1,$(".pagers").eq(0))}}),$("#icon-order-time").hover(function(){},function(){$(".visit-hover").hide()})},t.tmpl=function(){return $("#listTmpl").html()}(),t.getCommentList=function(e){var t=this,i=10,n=require("common/js/ajax"),a=require("common/js/pagination"),r=require("common/js/mustache.min");n({url:""+t.api+"/pc/evaluation/listonehos",type:"GET",datatype:"json",data:{key:$("input[name='key']").attr("data-value"),page:e,pageSize:i},success:function(i){if(0==i.status){if(i=i.data,i.commentList&&i.commentList.length){$(".comment-header").show(),$("#totalEcho").html(i.total);for(var n=i.commentList,o=n.length,s=null,l=0;o>l;++l)if(s=n[l],s.replyList&&s.replyList.length)s.hasCommment=!0;s=null}else $("#comment-total").html("暂无评价");$("#commentList").html(r.render(t.tmpl,i));var c=new a({total:i.total,pageSize:i.pageSize,curPage:e,pagerContainer:$(".pagers").eq(1),callback:function(e){t.getCommentList(e),c=null}});c.init()}},error:function(){$("#comment-total").remove()}})},t});
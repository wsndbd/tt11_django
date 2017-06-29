$(document).ready(function() {
    var pageno = parseInt($("#input_page").val());
    console.log("response$(document).ready(function() { ", pageno);
    $.ajax({
        url: "/goods_content/?pageno=" + pageno,
    }).done(function(response) {
        $("#div_goods_content").html(response);
    });
});

function reload_goods_list_pre_page() {
    var pageno = parseInt($("#input_page").val()) - 1;
    if (pageno < 1)
    {
        pageno = 1;
    }
    let url = "/goods/?pageno=" + pageno;
    let keyword = $("input[name = keyword]").val().trim();
    let type = parseInt($("#input_type").val());
    if (1 == type)
    {
        url += "&keyword=" + keyword;
    }
    window.location.href = url; 
}

function reload_goods_list(){
    var pageno = parseInt($("#select_pageno").val());
    window.location.href = "/goods/?pageno=" + pageno;
}

function reload_goods_list_next_page() {
    var pageno = parseInt($("#input_page").val()) + 1;
    window.location.href = "/goods/?pageno=" + pageno;
}

function click_search()
{
    var keyword = $("input[name = keyword]").val().trim();
    var pageno = parseInt($("#input_page").val());
    $.ajax({
        url: "/search_goods/?pageno=" + 1 + "&keyword=" + keyword,
    }).done(function(response) {
        console.log("response ", response);
        $("#div_goods_content").html(response);
        $("#input_type").html('<input type = "hidden" id = "input_type" value = "1">');
    });
}

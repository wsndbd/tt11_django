$(document).ready(function() {
    var pageno = parseInt($("#input_page").val());
    console.log("response$(document).ready(function() { ", pageno);
    $.ajax({
        url: "/goods_content/?pageno=" + pageno,
    }).done(function(response) {
        console.log("response ", response);
        $("#div_goods_content").html(response);
    });
});

function reload_goods_list_pre_page() {
    var pageno = parseInt($("#input_page").val()) - 1;
    if (pageno < 1)
    {
        pageno = 1;
    }

    window.location.href = "/goods/?pageno=" + pageno;
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
}

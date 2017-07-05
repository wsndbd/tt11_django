$(document).ready(function() {
    var pageno = parseInt($("#input_page").val());
    if (!pageno)
    {
        pageno = 1;
    }
    //console.log("response$(document).ready(function() { ", pageno);
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
    goto_page(pageno);    
}

function reload_goods_list(){
    var pageno = parseInt($("#select_pageno").val());
    goto_page(pageno);
}

function reload_goods_list_next_page() {
    var pageno = parseInt($("#input_page").val()) + 1;
    goto_page(pageno);
}

function click_search()
{
    var keyword = $("input[name = keyword]").val().trim();
    document.getElementById("input_page").value = 1;
    var pageno = parseInt($("#input_page").val());
    $.ajax({
        url: "/search_goods/?pageno=" + 1 + "&keyword=" + keyword,
    }).done(function(response) {
        $("#div_goods_content").html(response);
        document.getElementById("input_type").value = 1;
    });
}

function goto_page(pageno)
{
    let url = "/goods_content/?pageno=" + pageno;

    let type = parseInt($("#input_type").val());
    if (1 == type)
    {
        let keyword = $("input[name = keyword]").val().trim();
        url = "/search_goods/?pageno=" + pageno + "&keyword=" + keyword;
    }

    $.ajax({
        url: url,
    }).done(function(response) {
        $("#div_goods_content").html(response);
        document.getElementById("input_page").value = pageno;
    });
}

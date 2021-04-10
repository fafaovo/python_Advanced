//图片的淡出淡入效果
$(function () {
    $(".tu li").hover(function () {
        $(this).children(".mask").stop().fadeIn(1000);
    },function () {
        $(this).children(".mask").stop().fadeOut(1000);
    })
});
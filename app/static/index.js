// Script to provide view more/less functionality to reviews
$(".show-more a").on("click", function() {
    console.log("click");
    var $this = $(this);
    var $content = $this.parent().prev("div.content");
    var linkText = $this.text().toUpperCase();
    
    if (linkText === "SHOW MORE") {
        linkText = "Show less";
        $content.switchClass("hideContent", "showContent", 400);
    } else {
        linkText = "Show more";
        $content.switchClass("showContent", "hideContent", 400);
    };
    
    $this.text(linkText);
});
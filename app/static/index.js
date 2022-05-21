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


// Scroll to top button
const btn = document.querySelector("#btnScrollToTop");

btn.addEventListener("click", function() {

    // Animate the button to scroll smoothly to the top of the page
    $("html, body").animate({ scrollTop: 0}, "slow");
});
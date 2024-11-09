<script>
function openTab(evt, tabName) {
    // Hide all tab contents
    var i, tabcontent, tabbuttons;
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";  
    }
    // Remove active class from all buttons
    tabbuttons = document.getElementsByClassName("tab-button");
    for (i = 0; i < tabbuttons.length; i++) {
        tabbuttons[i].classList.remove("active");
    }
    // Show the current tab and add an active class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";  
    evt.currentTarget.classList.add("active");
}

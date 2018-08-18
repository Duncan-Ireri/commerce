var imgCount = 3;
        var dir = '../static/img/';
        var randomCount = Math.round(Math.random() * (imgCount - 1)) + 1;
        var images = new Array
                images[1] = "pexels-photo-264636.jpeg",
                images[2] = "wu-yi-136762-unsplash.jpg",
                images[3] = "rawpixel-755580-unsplash.jpg",
    document.getElementById("prod-back").style.backgroundImage = "url(" + dir + images[randomCount] + ")"; 

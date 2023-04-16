"use strict"
console.log('priver')
const ratings = document.querySelectorAll('.rating');

if (ratings.length > 0){
    initRatings();
}

function initRatings() {
    let ratingActive, ratingValue;
    for (let index = 0; index < ratings.length; index++){
        const rating = ratings[index];
        initRating(rating);
    }

    function initRating(rating){
        initRatingVars(rating);

        setRatingActiveWidth();

        if (rating.classList.contains('rating_set')){
            setRating(rating);
        }
    }

    function initRatingVars(rating){
        ratingActive = rating.querySelector('.rating_active');
        ratingValue = rating.querySelector('.rating_value');
    }

    function setRatingActiveWidth(index = ratingValue.innerHTML){
        const ratingActiveWidth = index / 0.05;
        ratingActive.style.width = `${ratingActiveWidth}%`;
    }

    function setRating(rating){
        const ratingItems = rating.querySelectorAll('.rating_item');

        for (let index = 0; index < ratingItems.length; index++){
            const ratingItem = ratingItems[index];
            
            ratingItem.addEventListener("mouseenter", function (e) {
                initRatingVars(rating);

                setRatingActiveWidth(ratingItem.value);
            });

            ratingItem.addEventListener("mouseleave", function(e) {
                setRatingActiveWidth();
            });

            ratingItem.addEventListener("click", function(e) {
                
                initRatingVars(rating);

                if (rating.dataset.ajax){
                    setRatingValue(ratingValue, rating);
                }
                else{
                    ratingValue.innerHTML = index + 1;
                    setRatingActiveWidth();
                }
            });
        }
    }
}
document.addEventListener('DOMContentLoaded', function() {
    // Get all elements in your page


let select = function () {
    let selectHeader = document.querySelectorAll('.select__header');
    let selectItem = document.querySelectorAll('.select__item');
    let selectBody = document.querySelectorAll('.select__body');

    selectHeader.forEach(item => {
        item.addEventListener('click', selectToggle 
        )
    });
    selectItem.forEach(item => {
        item.addEventListener('click', selectChoose)
    });

    function selectToggle() {
        this.parentElement.classList.toggle('is-active');
    }


    function selectChoose() {
        let text = this.innerText,
            select = this.closest('.select'),
            currentText = select.querySelector('.select__current');
        currentText.innerText = text;
        select.classList.remove('is-active');

    }

};


select();

let burger = document.getElementById('burger');
    burgerMenu = document.getElementById('burgerMenu');
    logo = document.getElementById('logo');
    navList = document.getElementById('navList');
burger.onclick = function() {
    burger.classList.toggle('is-active');
    burgerMenu.classList.toggle('is-active');
    logo.classList.toggle('is-active');
    navList.classList.toggle('is-active');
};
});

let btnLk = document.querySelector('#lk');
let formLk = document.querySelector('#lkForm');
let body = document.querySelector('body');
btnLk.addEventListener('click', function(){
    if(formLk.style.display == 'flex'){
        formLk.style.display = 'none';
        btnLk.style.transform = 'scale(1)'
    }
    else{
        btnLk.style.transform = 'scale(1.1)'
        formLk.style.display = 'flex';
    }
});
body.addEventListener('mousedown', function(e){
    if(!e.target.classList.contains('client__form') && !e.target.classList.contains('client__form-item') && !e.target.classList.contains('client__form-btn')){
        formLk.style.display = 'none';
        btnLk.style.transform = 'scale(1)'
    }
});

let cardAll =  document.querySelector('.card-link');
cardAll.forEach((card, key)=>{
    console.log(card, key);
    card.addEventListener('click', ()=>{
        console.log(key)
    })
})

//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiIiwic291cmNlcyI6WyJtYWluLmpzIl0sInNvdXJjZXNDb250ZW50IjpbImRvY3VtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ0RPTUNvbnRlbnRMb2FkZWQnLCBmdW5jdGlvbigpIHtcclxuICAgIC8vIEdldCBhbGwgZWxlbWVudHMgaW4geW91ciBwYWdlXHJcblxyXG5cclxubGV0IHNlbGVjdCA9IGZ1bmN0aW9uICgpIHtcclxuICAgIGxldCBzZWxlY3RIZWFkZXIgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcuc2VsZWN0X19oZWFkZXInKTtcclxuICAgIGxldCBzZWxlY3RJdGVtID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgnLnNlbGVjdF9faXRlbScpO1xyXG4gICAgbGV0IHNlbGVjdEJvZHkgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcuc2VsZWN0X19ib2R5Jyk7XHJcblxyXG4gICAgc2VsZWN0SGVhZGVyLmZvckVhY2goaXRlbSA9PiB7XHJcbiAgICAgICAgaXRlbS5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIHNlbGVjdFRvZ2dsZSBcclxuICAgICAgICApXHJcbiAgICB9KTtcclxuICAgIHNlbGVjdEl0ZW0uZm9yRWFjaChpdGVtID0+IHtcclxuICAgICAgICBpdGVtLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgc2VsZWN0Q2hvb3NlKVxyXG4gICAgfSk7XHJcblxyXG4gICAgZnVuY3Rpb24gc2VsZWN0VG9nZ2xlKCkge1xyXG4gICAgICAgIHRoaXMucGFyZW50RWxlbWVudC5jbGFzc0xpc3QudG9nZ2xlKCdpcy1hY3RpdmUnKTtcclxuICAgIH1cclxuXHJcblxyXG4gICAgZnVuY3Rpb24gc2VsZWN0Q2hvb3NlKCkge1xyXG4gICAgICAgIGxldCB0ZXh0ID0gdGhpcy5pbm5lclRleHQsXHJcbiAgICAgICAgICAgIHNlbGVjdCA9IHRoaXMuY2xvc2VzdCgnLnNlbGVjdCcpLFxyXG4gICAgICAgICAgICBjdXJyZW50VGV4dCA9IHNlbGVjdC5xdWVyeVNlbGVjdG9yKCcuc2VsZWN0X19jdXJyZW50Jyk7XHJcbiAgICAgICAgY3VycmVudFRleHQuaW5uZXJUZXh0ID0gdGV4dDtcclxuICAgICAgICBzZWxlY3QuY2xhc3NMaXN0LnJlbW92ZSgnaXMtYWN0aXZlJyk7XHJcblxyXG4gICAgfVxyXG5cclxufTtcclxuXHJcblxyXG5zZWxlY3QoKTtcclxuXHJcbmxldCBidXJnZXIgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYnVyZ2VyJyk7XHJcbiAgICBidXJnZXJNZW51ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2J1cmdlck1lbnUnKTtcclxuICAgIGxvZ28gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnbG9nbycpO1xyXG4gICAgbmF2TGlzdCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCduYXZMaXN0Jyk7XHJcbmJ1cmdlci5vbmNsaWNrID0gZnVuY3Rpb24oKSB7XHJcbiAgICBidXJnZXIuY2xhc3NMaXN0LnRvZ2dsZSgnaXMtYWN0aXZlJyk7XHJcbiAgICBidXJnZXJNZW51LmNsYXNzTGlzdC50b2dnbGUoJ2lzLWFjdGl2ZScpO1xyXG4gICAgbG9nby5jbGFzc0xpc3QudG9nZ2xlKCdpcy1hY3RpdmUnKTtcclxuICAgIG5hdkxpc3QuY2xhc3NMaXN0LnRvZ2dsZSgnaXMtYWN0aXZlJyk7XHJcbn07XHJcbn0pOyJdLCJmaWxlIjoibWFpbi5qcyJ9
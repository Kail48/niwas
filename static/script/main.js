const navSlide=()=>{
    const burger=document.querySelector(".burger");
    const nav=document.querySelector(".nav_links");
    const navLinks=document.querySelectorAll('.nav_links li');
    burger.addEventListener('click',()=>{
        console.log('script is working')
        nav.classList.toggle('nav_active');
        burger.classList.toggle('toggle');
        navLinks.forEach((link,index)=>{
            if(link.style.animation){
                link.style.animation=''
            }
            else{
                link.style.animation=`navLinkFade 0.5s ease forwards ${index/7}s`
            }
        });
    });
    
}
navSlide();
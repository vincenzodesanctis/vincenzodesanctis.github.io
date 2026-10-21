console.log("🟢 Script Lightbox caricato con successo!");

document.addEventListener('click', function(e) {
    const link = e.target.closest('a.glightbox');
    
    if (link) {
        e.preventDefault(); 
        console.log("🟢 Click intercettato su un'immagine.");
        
        if (typeof GLightbox !== 'undefined') {
            const gallerySlug = link.getAttribute('data-gallery');
            const links = document.querySelectorAll('a.glightbox[data-gallery="' + gallerySlug + '"]');
            
            const elements = Array.from(links).map(a => ({
                href: a.getAttribute('href'),
                type: 'image'
            }));
            
            const index = Array.from(links).indexOf(link);

            if (!window.myLightbox) {
                window.myLightbox = GLightbox({
                    touchNavigation: true,
                    loop: true,
                    zoomable: true
                });
            }
            
            window.myLightbox.setElements(elements);
            window.myLightbox.openAt(index);
        } else {
            console.error("🔴 ERRORE: La libreria GLightbox non è stata caricata.");
        }
    }
});

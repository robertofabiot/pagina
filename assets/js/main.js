/*
	Industrious by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
*/
(function($) {

	var	$window = $(window),
		$banner = $('#banner'),
		$body = $('body');

	// Breakpoints.
		breakpoints({
			default:   ['1681px',   null       ],
			xlarge:    ['1281px',   '1680px'   ],
			large:     ['981px',    '1280px'   ],
			medium:    ['737px',    '980px'    ],
			small:     ['481px',    '736px'    ],
			xsmall:    ['361px',    '480px'    ],
			xxsmall:   [null,       '360px'    ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Menu.
		$('#menu')
			.append('<a href="#menu" class="close"></a>')
			.appendTo($body)
			.panel({
				target: $body,
				visibleClass: 'is-menu-visible',
				delay: 500,
				hideOnClick: true,
				hideOnSwipe: true,
				resetScroll: true,
				resetForms: true,
				side: 'right'
			});

})(jQuery);

/* --- Lógica de Envío de Formulario con EmailJS --- */

(function($) {

    // Esperar a que el DOM esté listo
    $(function() {
        
        // Seleccionamos el formulario por su ID
        $('#contact-form').on('submit', function(event) {
            event.preventDefault(); // Evita que la página se recargue

            // Referencia al botón para cambiarle el texto
            var btn = $(this).find('button[type="submit"]');
            var btnText = btn.text();
            
            // Cambiar texto a "Enviando..."
            btn.text('Enviando...').addClass('disabled');

            // Parámetros: Service ID, Template ID, Elemento Formulario (this)
            // REEMPLAZA LOS IDs CON LOS TUYOS
            emailjs.sendForm('service_h8nd5qy', 'template_1qdckht', this)
                .then(function() {
                    // Éxito
                    alert('¡Mensaje enviado con éxito! Nos pondremos en contacto pronto.');
                    $('#contact-form')[0].reset(); // Limpia el formulario
                    btn.text(btnText).removeClass('disabled'); // Restaura el botón
                }, function(error) {
                    // Error
                    console.log('FAILED...', error);
                    alert('Hubo un error al enviar el mensaje. Por favor intenta de nuevo.');
                    btn.text(btnText).removeClass('disabled');
                });
        });

    });

})(jQuery);

/* --- Lógica del Carrusel --- */
(function() {
    let slides = document.getElementsByClassName("carousel-slide");
    if (slides.length === 0) return;

    let slideIndex = 1;
    showSlides(slideIndex);

    window.plusSlides = function(n) {
        showSlides(slideIndex += n);
    };

    window.currentSlide = function(n) {
        showSlides(slideIndex = n);
    };

    function showSlides(n) {
        let i;
        let dots = document.getElementsByClassName("dot");
        if (n > slides.length) {slideIndex = 1}    
        if (n < 1) {slideIndex = slides.length}
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex-1].style.display = "block";  
        if (dots.length > 0) {
            dots[slideIndex-1].className += " active";
        }
    }
})();

/* --- Lógica de Scroll Reveal --- */
(function() {
    document.addEventListener("DOMContentLoaded", function() {
        // Seleccionamos elementos que queremos animar
        const elementsToReveal = document.querySelectorAll('.service-card, .highlights section, .contact-card, .feature-section .col-6, #cta .inner');
        
        // Añadimos la clase base
        elementsToReveal.forEach(el => el.classList.add('reveal-on-scroll'));

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        elementsToReveal.forEach(el => observer.observe(el));
    });
})();
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
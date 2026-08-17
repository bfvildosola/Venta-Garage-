import os
import json
import glob

# =========================================================
# 🔴 1. CONFIGURACIÓN DE CONTACTO Y CONEXIONES
# =========================================================
NUMERO_WHATSAPP = "56975593099" 
LINK_GOOGLE_APPS_SCRIPT = "https://script.google.com/macros/s/AKfycbw4YErtXDU2VyJlH659HPeWxmmTPkE38tNsFnwhc5fRBBaL1tNiojqvB78k4YgdECztYQ/exec"

# =========================================================
# 🟢 2. LISTA DE PRECIOS Y ASIGNACIÓN DE FOTOS
# =========================================================
precios_definidos = {
    "ski_stockli": 900000, "ski_volkl": 280000, "ski_kastle": 350000, "ski_rossignol": 220000,
    "ski_head": 130000, "ski_armada": 90000, "ski_dynastar": 90000, "botas_dalbello": 120000,
    "botas_nordica": 90000, "botas_tecnica_azul": 90000, "botas_tecnica_amarilla": 90000,
    "casco_diezz": 290000, "antiparras_alpina": 52500, "protector_slytech": 42500,
    "bastones_gabel": 13990, "bastones_salomon": 18500, "bastones_kerma": 15000,
    "bike_specialized_1": 3100000, "bike_2": 3100000, "kitesurf_best": 120000, "tabla_wayo": 160000,
    "tv_samsung_frame": 1100000, "monitor_samsung": 250000, "apple_imac": 250000,
    "apple_tv": 100000, "parlantes_mirage": 230000, "lente_tamron_70_200": 330000,
    "lente_sigma_17_50": 170000, "impresora_brother": 60000, "maquina_humo": 20000,
    "chaqueta_rossignol": 75000, "parka_lippi": 35000, "pantalon_trangoworld": 40000,
    "chaqueta_footjoy": 37500, "polera_footjoy": 20000, "pantalon_naturehike": 40000,
    "poleron_tnf": 25000, "aire_kendal": 90000, "cooler_azul_ruedas": 35000,
    "cooler_coleman_rojo": 25000, "cooler_rubbermaid_blanco": 30000, "cooler_rubbermaid_rojo": 18000,
    "cooler_klack_azul": 15000, "porton_madera": 250000, "rampa_moto": 42500, "espejo_textil": 25000,
    "cadenas_nieve_power": 45000, "cadenas_nieve_tacoma": 45000, "home_theater_yamaha": 350000,
    "pack_fox_enduro": 95000, "remadora_waterrower": 550000, "banca_fullfit": 150000,      
    "tv_samsung_curvo": 250000, "lavadora_samsung": 350000,
    "refrigerador_samsung": 300000, "refrigerador_fdv": 680000, "comedor_vidrio_madera": 600000,
    "sillon_milk": 680000,
    
    # NUEVOS ARTÍCULOS
    "sillon_cuero_3c": 350000,
    "sitial_cuero": 130000,
    "horno_oster_airfryer": 80000
}

asignaciones = {
  "ski_stockli": ["20260802_153721.jpg", "20260802_153658.jpg", "20260802_153706.jpg", "20260802_153716.jpg"],
  "ski_volkl": ["20260802_154039.jpg", "20260802_154058.jpg", "20260802_154053.jpg", "20260802_154049.jpg", "20260802_154044.jpg"],
  "ski_kastle": ["20260802_153706.jpg", "20260802_153716.jpg"],
  "ski_rossignol": ["20260802_153740.jpg", "20260802_153748.jpg", "20260802_153822.jpg"],
  "ski_head": ["20260802_154339.jpg"],
  "ski_armada": ["20260802_153858.jpg"],
  "ski_dynastar": ["20260802_161716.jpg", "20260802_161724.jpg", "20260802_161726.jpg", "20260802_161730 2.jpg", "20260802_161730.jpg", "20260802_161734 2.jpg", "20260802_161734.jpg"],
  "botas_dalbello": ["20260802_171614.jpg", "20260802_171622.jpg", "20260802_171630.jpg", "20260802_171648.jpg", "20260802_171652.jpg", "20260802_172853.jpg"],
  "botas_nordica": ["20260802_171714.jpg", "20260802_171720.jpg", "20260802_171727.jpg", "20260802_171731.jpg", "20260802_171739.jpg", "20260802_172815.jpg"],
  "botas_tecnica_azul": ["20260802_171545.jpg", "20260802_171552.jpg", "20260802_171601.jpg", "20260802_172835.jpg", "20260802_172837.jpg"],
  "botas_tecnica_amarilla": ["20260802_171505.jpg", "20260802_171514.jpg", "20260802_171531.jpg", "20260802_172826.jpg"],
  "casco_diezz": ["20260802_171805.jpg", "20260802_171808.jpg", "20260802_171810.jpg", "20260802_171819.jpg", "20260802_171827.jpg"],
  "antiparras_alpina": ["20260802_172907.jpg"],
  "protector_slytech": ["20260802_172149.jpg", "20260802_172155.jpg"],
  "bastones_gabel": ["20260802_161700.jpg", "20260802_161704.jpg", "20260802_161706.jpg"],
  "bastones_salomon": ["20260802_154430.jpg", "20260802_154417.jpg"],
  "bastones_kerma": ["20260802_154420.jpg"],
  "bike_specialized_1": ["20260802_154813.jpg", "20260802_154822.jpg", "20260802_154837.jpg", "20260802_154853.jpg", "20260802_154856.jpg", "20260802_154900.jpg", "A8A16984-BCFE-47BB-9493-D4B0C23D9894_1_105_c.jpg"],
  "bike_2": ["20260802_155531.jpg", "20260802_155537.jpg", "20260802_155541.jpg", "20260802_155548.jpg", "20260802_155552.jpg", "20260802_155557.jpg", "83FED23D-936D-428F-AD26-E1B8A3381390_1_105_c.jpg"],
  "kitesurf_best": ["20260802_155639.jpg", "20260802_155654.jpg"],
  "tabla_wayo": ["20260802_162201.jpg", "20260802_162208.jpg", "20260802_162212.jpg", "20260802_162216.jpg", "20260802_162218.jpg", "20260802_162223.jpg", "20260802_162226.jpg", "20260802_162240.jpg"],
  "tv_samsung_frame": ["20260802_164030.jpg", "20260802_164036.jpg", "20260802_164045.jpg", "20260802_164048.jpg"],
  "monitor_samsung": ["20260802_165339.jpg", "20260802_165343.jpg", "20260802_170554.jpg", "20260802_170600.jpg", "20260802_170607.jpg"],
  "apple_imac": ["20260802_165057.jpg", "20260802_165102.jpg", "20260802_165114.jpg", "843097BD-99C4-4391-AC90-1D18C755CA6D_1_105_c.jpeg", "BCBA540E-B8D1-45DE-9548-FBD2DD5EA252_1_105_c.jpeg"],
  "apple_tv": ["20260802_165408.jpg", "20260802_165414.jpg", "20260802_165419.jpg"],
  "parlantes_mirage": ["20260802_164111.jpg", "20260802_164114.jpg", "20260802_164136.jpg", "20260802_164143.jpg"],
  "lente_tamron_70_200": ["20260802_170020.jpg", "20260802_170027.jpg", "20260802_170034.jpg", "20260802_170044.jpg"],
  "lente_sigma_17_50": ["20260802_170058.jpg", "20260802_170106.jpg", "20260802_170116.jpg", "20260802_170122.jpg"],
  "impresora_brother": ["20260802_170211.jpg"],
  "maquina_humo": ["20260802_160213.jpg", "20260802_160224.jpg", "20260802_160233.jpg"],
  "chaqueta_rossignol": ["20260802_172004.jpg", "20260802_172009.jpg", "20260802_172016.jpg", "20260802_172043.jpg"],
  "parka_lippi": ["20260802_172454.jpg", "20260802_172456.jpg", "20260802_172505.jpg", "20260802_172509.jpg", "20260802_172522.jpg", "20260802_172525.jpg"],
  "pantalon_trangoworld": ["20260802_172055.jpg", "20260802_172104.jpg", "20260802_172116.jpg", "20260802_172120.jpg"],
  "polera_footjoy": ["20260802_172704.jpg", "20260802_172706.jpg", "20260802_172723.jpg", "20260802_172727.jpg", "20260802_172753.jpg"],
  "pantalon_naturehike": ["20260802_172919.jpg", "20260802_172923.jpg", "20260802_172934.jpg"],
  "poleron_tnf": ["20260802_172337.jpg", "20260802_172341.jpg", "20260802_172354.jpg"],
  "aire_kendal": ["20260802_155429.jpg", "20260802_155435.jpg"],
  "cooler_azul_ruedas": ["20260802_160706.jpg", "20260802_160712.jpg", "20260802_160727.jpg"],
  "cooler_coleman_rojo": ["20260802_160429.jpg", "20260802_160443.jpg", "20260802_160456.jpg", "20260802_160500.jpg"],
  "cooler_rubbermaid_blanco": ["20260802_162453.jpg", "20260802_162456.jpg"],
  "porton_madera": ["20260802_153230.jpg"],
  "rampa_moto": ["20260802_154618.jpg", "20260802_154624.jpg", "20260802_154628.jpg"],
  "espejo_textil": ["20260802_154506.jpg", "20260802_154504.jpg", "20260802_154513.jpg"],
  "cadenas_nieve_power": ["EE8080A1-AF38-4CDE-AC0A-FA0A9449102B_1_105_c.jpeg", "E519B17F-DC74-41F4-9A67-01D271B7A4C9_1_105_c.jpeg"],
  "cadenas_nieve_tacoma": ["192B5AAF-A963-48E7-9322-903E081BA796_1_105_c.jpg"],
  "home_theater_yamaha": ["3FEFD175-023B-412F-A1D8-DA224A2890C0_1_105_c.jpeg", "22B37D59-240B-4615-B2B1-13950706212A_1_105_c.jpeg", "8AC0308D-3746-4558-9303-33E66B21FDFF_1_105_c.jpg", "FD5C9AD4-C482-4337-A498-526311811076_1_105_c.jpg", "43A603B3-7987-4800-AAEC-9799295DBEB5_1_105_c.jpeg"],
  "pack_fox_enduro": ["0B62D3B3-FEE6-4061-97F8-216BD9EF117A_1_105_c.jpg", "5B092798-A589-465D-AA93-9093EA3E80B5_1_105_c.jpeg", "C949E4E0-AD65-4FF9-8E0C-0D060B2641A7_1_105_c.jpeg"],
  "remadora_waterrower": ["60E11074-192B-4E2D-8543-7470373BDCEE_1_105_c.jpeg", "E34BFCA6-D536-473B-9139-A4D9FA9EF0A6_1_105_c.jpeg", "7F886CD9-CE16-4B40-98BB-BD9D4D2A731D_1_105_c.jpeg"],
  "banca_fullfit": ["1B98C2CD-BDD1-49D7-8083-55D8B818E845_1_105_c.jpeg", "A43E0409-CC33-4934-BA78-716099A9BB7B_1_105_c.jpeg", "0A722E56-FADC-4749-88D0-EC5F3047004F_1_105_c.jpeg"],
  "tv_samsung_curvo": ["3EE1128D-9F3E-49FF-A9B2-60902F824971_1_105_c.jpeg", "33113E0D-A591-4E46-AC76-BF5DD65605B7_1_105_c.jpg", "EA722B7E-4B00-4626-B98E-4F5C0D418CCC_1_105_c.jpg"],
  "lavadora_samsung": ["51546376-A4A0-44C4-8D79-F2CAECA16315_1_105_c.jpg", "5140EFFD-3690-49D4-9A6B-F23E7945B1BD_1_105_c.jpeg", "DD1A470B-6523-43B8-A2D6-9691B804DCCC_1_105_c.jpeg", "3761ED9C-D842-4B78-B1D6-F2E4A5020369_1_105_c.jpg"],
  "refrigerador_samsung": ["278792DE-5228-4CB7-81F2-E0FDDFA56C25_1_105_c.jpeg"],
  "refrigerador_fdv": ["47840D65-7D52-4304-8935-C50032FBC71D_1_105_c.jpeg", "80D72623-63B1-40B4-8C89-F9505DEE8969_1_105_c.jpeg"],
  "comedor_vidrio_madera": ["WhatsApp Image 2026-08-15 at 18.31.10.jpg", "WhatsApp Image 2026-08-15 at 18.31.11 (1).jpg", "WhatsApp Image 2026-08-15 at 18.31.11.jpg", "WhatsApp Image 2026-08-15 at 18.31.10 (4).jpg", "WhatsApp Image 2026-08-15 at 18.31.10 (3).jpg", "WhatsApp Image 2026-08-15 at 18.31.10 (2).jpg", "WhatsApp Image 2026-08-15 at 18.31.10 (1).jpeg"],
  "sillon_milk": ["WhatsApp Image 2026-08-15 at 18.34.11 (1).jpg", "WhatsApp Image 2026-08-15 at 18.34.11.jpg", "WhatsApp Image 2026-08-15 at 18.34.10 (5).jpg", "WhatsApp Image 2026-08-15 at 18.34.10 (4).jpg", "WhatsApp Image 2026-08-15 at 18.34.10 (3).jpg", "WhatsApp Image 2026-08-15 at 18.34.10.jpeg"],
  
  # FOTOS NUEVAS
  "sillon_cuero_3c": ["WhatsApp Image 2026-08-07 at 11.42.56.jpeg"],
  "sitial_cuero": ["WhatsApp Image 2026-08-07 at 11.42.56 (1).jpeg"],
  "horno_oster_airfryer": ["WhatsApp Image 2026-08-04 at 18.53.35.jpeg", "WhatsApp Image 2026-08-04 at 18.53.54.jpeg"]
}

# =========================================================
# 🔵 3. CATÁLOGO CON DESCIPCIONES ENRIQUECIDAS
# =========================================================
catalogo = [
    {
        "categoria": "1. Deportes de Nieve (Esquí & Snowboard)",
        "subcategorias": [
            {
                "nombre": "1.1. Skis Premium (Alta Gama)",
                "items": [
                    {"id": "ski_stockli", "titulo": "Skis Stöckli Montero AX - 168 cm", "specs": "<strong>Reseña:</strong> Fabricados a mano en Suiza. El Montero AX es famoso por combinar la agilidad de un esquí de slalom con la estabilidad absoluta del freeride.<br><br><strong>Ficha Técnica:</strong> Longitud: 168 cm | Estructura: Titanal & Núcleo de Madera Ligera | Fijaciones incluidas."},
                    {"id": "ski_volkl", "titulo": "Skis Völkl Mantra V.Werks Carbon - 170 cm", "specs": "<strong>Reseña:</strong> Una auténtica obra de arte de la ingeniería en carbono. Extremadamente ligeros para el ascenso pero súper potentes en el descenso.<br><br><strong>Ficha Técnica:</strong> Longitud: 170 cm | Construcción: Carbono 3D.RIDGE | Incluye fijaciones Marker Griffon."},
                    {"id": "ski_kastle", "titulo": "Skis Kästle BMX 105 Freeride - 173 cm", "specs": "<strong>Reseña:</strong> El rey indiscutido del freeride. La icónica ventana transparente en la espátula (Hollowtech) no es solo estética: elimina peso y reduce drásticamente el rebote del esquí.<br><br><strong>Ficha Técnica:</strong> Longitud: 173 cm | Patín: 105 mm | Fijaciones: Marker Griffon 13."}
                ]
            },
            {
                "nombre": "1.2. Skis All-Mountain & Pista",
                "items": [
                    {"id": "ski_rossignol", "titulo": "Skis Rossignol Experience 80 Carbon - 166 cm", "specs": "<strong>Reseña:</strong> El balance perfecto para esquiadores intermedios-avanzados. Reforzado con carbono para darte respuesta inmediata sin exigir el esfuerzo físico de un esquí de competición.<br><br><strong>Ficha Técnica:</strong> Longitud: 166 cm | Patín: 80 mm | Núcleo: Paulownia Wood Core con Carbono."},
                    {"id": "ski_head", "titulo": "Skis Head Total JOY SLR (Mujer)", "specs": "<strong>Reseña:</strong> Diseñados específicamente para mujeres, utilizando tecnología Graphene. Son súper permisivos, fáciles de girar y evitan la fatiga en las piernas.<br><br><strong>Ficha Técnica:</strong> Construcción: LIBRA Graphene & Karuba Wood Core | Incluye fijaciones ajustables."},
                    {"id": "ski_armada", "titulo": "Skis Freeride Armada ARV 96", "specs": "<strong>Reseña:</strong> El esquí más icónico de freestyle/freeride. Su perfil Rocker permite saltar en el park o esquiar de espaldas.<br><br><strong>Ficha Técnica:</strong> Perfil: AR Freeride Rocker Twin Tip | Canto reforzado 2.5 Impact Edge."},
                    {"id": "ski_dynastar", "titulo": "Skis Dynastar Speed Team Course WC - 160 cm", "specs": "<strong>Reseña:</strong> Un esquí de linaje de Copa del Mundo adaptado para pista. Está pensado para quienes aman bajar rápido y hacer giros cortos y precisos en nieve dura o hielo.<br><br><strong>Ficha Técnica:</strong> Longitud: 160 cm | Estructura: Sandwich Titanal de Competición."}
                ]
            },
            {
                "nombre": "1.3. Botas, Cascos y Accesorios",
                "items": [
                    {"id": "botas_dalbello", "titulo": "Botas de Ski Dalbello Boss 110", "specs": "<strong>Reseña:</strong> Su famoso diseño Cabrio de 3 piezas permite una flexión hacia adelante muy progresiva y suave, protegiendo tus canillas.<br><br><strong>Ficha Técnica:</strong> Flex: 110 (Avanzado) | Horma ancha: 103 mm | Hebillas microajustables."},
                    {"id": "botas_nordica", "titulo": "Botas de Ski Nordica Cruise 75", "specs": "<strong>Reseña:</strong> Priorizan el confort absoluto y el calor. Ideales para esquiadoras principiantes o intermedias.<br><br><strong>Ficha Técnica:</strong> Flex: 75 | Tamaño: 295 mm (~25.0 Mondo) | Suela de alta tracción."},
                    {"id": "botas_tecnica_azul", "titulo": "Botas Tecnica Mach1 MV 110 (Azul/Naranja)", "specs": "<strong>Reseña:</strong> Reconocidas en el mercado por su sistema C.A.S., que permite a los bootfitters adaptar la carcasa exactamente a la forma de tu pie.<br><br><strong>Ficha Técnica:</strong> Flex: 110 | Tamaño: 306 mm (26.0 - 26.5 Mondo)."},
                    {"id": "botas_tecnica_amarilla", "titulo": "Botas Tecnica Ten.2 80 (Amarillo/Negro)", "specs": "<strong>Reseña:</strong> Bota todoterreno muy cómoda gracias a su sistema Quick Instep, que suaviza el plástico en el empeine.<br><br><strong>Ficha Técnica:</strong> Flex: 80 | Tamaño: 26.5 Mondo | Horma: 102 mm."},
                    {"id": "casco_diezz", "titulo": "Casco Diezz Activlux Visor Photochromic", "specs": "<strong>Reseña:</strong> Olvídate de cambiar antiparras. Este casco premium francés trae una visera integrada fotocromática que se oscurece automáticamente si hay sol.<br><br><strong>Ficha Técnica:</strong> Construcción In-Mold ultraligera | Visera S1-S3 adaptable."},
                    {"id": "antiparras_alpina", "titulo": "Antiparras Alpina Double Jack Mag Q-LITE", "specs": "<strong>Reseña:</strong> Cuentan con un lente imantado magnético. Puedes quitar el lente oscuro y poner el claro en un segundo, sin sacarte los guantes.<br><br><strong>Ficha Técnica:</strong> Lente Magnético intercambiable | Filtro Q-LITE de alto contraste."},
                    {"id": "protector_slytech", "titulo": "Protector Columna Slytech Backpro", "specs": "<strong>Reseña:</strong> Seguridad nivel pro. Su espuma inteligente es blanda al moverse y respirar, pero se endurece como una roca al recibir un impacto.<br><br><strong>Ficha Técnica:</strong> Talla: L | Material: Espuma inteligente 2ND SKIN HD en formato chaleco."},
                    {"id": "bastones_gabel", "titulo": "Bastones de Ski Gabel Speed (Par)", "specs": "<strong>Reseña:</strong> Bastones italianos de alta velocidad, construidos en una aleación resistente que evita que se doblen o partan con facilidad.<br><br><strong>Ficha Técnica:</strong> Tubo: Aleación de Aluminio F56 | Puntera de acero reforzado."},
                    {"id": "bastones_salomon", "titulo": "Bastones de Ski Salomon Arctic S3", "specs": "<strong>Reseña:</strong> Clásicos, ligeros y altamente confiables. El strap de seguridad S3 se suelta automáticamente si el bastón se engancha en un árbol.<br><br><strong>Ficha Técnica:</strong> Tubo: Aluminio 6061 | Empuñadura bi-material."},
                    {"id": "bastones_kerma", "titulo": "Bastones de Ski Kerma Vector Carbon", "specs": "<strong>Reseña:</strong> Muy ligeros al balanceo gracias a su mezcla de carbono y aluminio. Reducen la fatiga de los brazos en jornadas de esquí largas.<br><br><strong>Ficha Técnica:</strong> Aleación ligera de carbono y fibra | Puntera de acero al tungsteno."}
                ]
            }
        ]
    },
    {
        "categoria": "2. Vehículos, Ciclismo & Outdoor",
        "subcategorias": [
            {
                "nombre": "2.1. Cadenas de Nieve para Vehículos",
                "items": [
                    {"id": "cadenas_nieve_power", "titulo": "Cadenas de Nieve Power para Barro y Nieve", "specs": "<strong>Reseña:</strong> Indispensables para subir a la montaña o enfrentar terrenos difíciles. Cadenas de tipo 'Bar Reinforced' (barras de refuerzo) diseñadas para máxima tracción en hielo y barro profundo.<br><br><strong>Ficha Técnica:</strong> Compatibilidad principal (Stock No. 1884): 265/60/R15, 265/70/R15, 245/75/R16, 255/70/R16, 245/65/R17, 255/65/R17, 255/60/R18 y similares."},
                    {"id": "cadenas_nieve_tacoma", "titulo": "Cadenas de Nieve 265/75/R16 (Tacoma)", "specs": "<strong>Reseña:</strong> Set de cadenas de nieve/barro de alto agarre, almacenadas en estuche rígido azul. Perfectas para camionetas tipo Toyota Tacoma u otros vehículos 4x4 con la medida específica.<br><br><strong>Ficha Técnica:</strong> Medida específica soportada: 265/75/R16. Construcción en acero duradero."}
                ]
            },
            {
                "nombre": "2.2. Bicicletas y Accesorios",
                "items": [
                    {"id": "bike_specialized_1", "titulo": "E-Bike Specialized Turbo Creo SL Comp Carbon + Kit", "specs": "<strong>Reseña:</strong> Una de las mejores e-bikes de gravel/ruta del mundo. Su motor SL 1.1 es tan silencioso y la bici tan ligera, que te olvidarás de que es eléctrica. Ofrece una autonomía tremenda y suaviza los baches con su suspensión en el manubrio Future Shock 2.0. <br><br><strong>Ficha Técnica:</strong> Carbono FACT 11r | Motor 240W | Batería 320Wh | Transmisión Shimano GRX.<br><strong>⚡ INCLUYE KIT:</strong> Casco Specialized Blanco, cargador original y guantes."},
                    {"id": "bike_2", "titulo": "Bicicleta BMC Speedfox Carbon Double Suspension + Kit", "specs": "<strong>Reseña:</strong> Una máquina suiza para trail. Escala montañas con la eficiencia de una bici de Cross Country, pero desciende con la agresividad de una Enduro. Su sistema de doble suspensión APS absorbe todo sin hacerte perder energía al pedalear.<br><br><strong>Ficha Técnica:</strong> Cuadro Carbono Doble Suspensión | Horquilla Fox 34 | Transmisión SRAM Eagle 12V.<br><strong>⚡ INCLUYE KIT:</strong> Casco Specialized Negro, cargador original y guantes cortos."},
                    {"id": "pack_fox_enduro", "titulo": "Pack Enduro/Descenso FOX (Casco Integral + Rodilleras)", "specs": "<strong>Reseña:</strong> La protección definitiva para los amantes de los descensos y el enduro. El casco integral Fox ofrece ventilación superior y protección completa de mandíbula, mientras que las rodilleras aseguran movilidad sin sacrificar seguridad ante impactos.<br><br><strong>Ficha Técnica:</strong> Incluye: 1 Casco integral FOX (gris mate) + 1 Par de Rodilleras FOX Pro."}
                ]
            },
            {
                "nombre": "2.3. Deportes de Agua",
                "items": [
                    {"id": "kitesurf_best", "titulo": "Set Kitesurf Best Waroo 9m² Completo", "specs": "<strong>Reseña:</strong> El Best Waroo revolucionó el kitesurf con su diseño SLE (Supported Leading Edge), ofreciendo un rango de viento gigante y un relanzamiento desde el agua facilísimo. Perfecto tanto para principiantes como para expertos en saltos altos.<br><br><strong>Ficha Técnica:</strong> Superficie: 9 m² | Incluye barra de control, líneas, arnés, bomba y mochila."},
                    {"id": "tabla_wayo", "titulo": "Tabla de Surf Wayo Whilar + Accesorios", "specs": "<strong>Reseña:</strong> Tabla shappeada por la reconocida marca peruana Wayo Whilar. Su diseño All-Round (todoterreno) te permite surfear desde olas pequeñas y fofas hasta paredes más paradas con gran estabilidad y velocidad de remada.<br><br><strong>Ficha Técnica:</strong> Setup de 3 Quillas desmontables | Incluye Leash de seguridad y funda acolchada."}
                ]
            }
        ]
    },
    {
        "categoria": "3. Tecnología, Audio & Fotografía",
        "subcategorias": [
            {
                "nombre": "3.1. Equipos de Audio",
                "items": [
                    {"id": "home_theater_yamaha", "titulo": "Sistema Home Theater Yamaha YST + Receiver", "specs": "<strong>Reseña:</strong> Un cine en casa completo y potente. Este sistema incluye el robusto Subwoofer Activo Yamaha YST-SW315 con tecnología Advanced YST para bajos profundos, un potente Receiver AV, y los canales (parlante central y satélites) necesarios para lograr un sonido envolvente inmersivo de altísima calidad.<br><br><strong>Ficha Técnica:</strong> Incluye: 1 Receiver AV Yamaha, 1 Subwoofer Activo YST-SW315 (250W), 1 Parlante Central y parlantes satélite. Controles de corte de frecuencia y bajos en el subwoofer."},
                    {"id": "parlantes_mirage", "titulo": "Parlantes Columna Hi-Fi Mirage FRx-7 (Par)", "specs": "<strong>Reseña:</strong> Altavoces audiófilos de culto. Su tecnología omnipolar dispersa el sonido en 360 grados, creando una escena de audio envolvente que te hace sentir en medio de un concierto en vivo, sin importar dónde te sientes en la sala.<br><br><strong>Ficha Técnica:</strong> Diseño Columna Bipolar/Omnipolar | Potencia: 150W RMS | Respuesta: 33Hz - 22kHz."}
                ]
            },
            {
                "nombre": "3.2. Electrónica General",
                "items": [
                    {"id": "tv_samsung_frame", "titulo": "Smart TV Samsung The Frame 75\" QLED 4K", "specs": "<strong>Reseña:</strong> Espectacular obra de diseño. Cuando la apagas, se convierte en un cuadro de arte real (no parece una pantalla). Su panel Matte Display elimina el 100% de los reflejos de las ventanas, y su One Connect Box saca todo el cablerío de la vista.<br><br><strong>Ficha Técnica:</strong> 75 pulgadas QLED 4K | Incluye One Connect Box y soporte de pared No Gap."},
                    {"id": "tv_samsung_curvo", "titulo": "Smart TV Samsung Pantalla Curva", "specs": "<strong>Reseña:</strong> Un televisor diseñado para sumergirte en la acción. Su panel curvo mejora los ángulos de visión y reduce la fatiga ocular, creando un contraste más uniforme. Ideal para disfrutar de noches de películas o videojuegos en la sala de estar con una sensación de profundidad envolvente.<br><br><strong>Ficha Técnica:</strong> Pantalla LED Curva Samsung | Múltiples puertos HDMI y USB integrados en el panel trasero."},
                    {"id": "monitor_samsung", "titulo": "Monitor Curvo Samsung ViewFinity S65UA 34\"", "specs": "<strong>Reseña:</strong> Incrementa tu productividad brutalmente. Su formato Ultra-Wide curvo equivale a tener dos monitores pegados sin bordes molestos. Cuenta con USB-C que transmite imagen y carga tu notebook al mismo tiempo con un solo cable.<br><br><strong>Ficha Técnica:</strong> Resolución Ultra-WQHD (3440 x 1440) 21:9 | Curvatura inmersiva 1000R | 100Hz."},
                    {"id": "apple_imac", "titulo": "Apple iMac Slim All-in-One", "specs": "<strong>Reseña:</strong> El clásico de Apple en su icónico diseño de aluminio extra delgado. Ideal para edición de documentos, ofimática y diseño ligero. Su pantalla ofrece colores vibrantes que no cansan la vista y mantiene tu escritorio libre de cables.<br><br><strong>Ficha Técnica:</strong> Pantalla Retina | Almacenamiento SSD rápido | Incluye Apple Magic Keyboard (Teclado) y Magic Mouse originales."},
                    {"id": "apple_tv", "titulo": "Apple TV 4K HDR 64GB", "specs": "<strong>Reseña:</strong> Transforma cualquier tele en el sistema más rápido y fluido del mercado. A diferencia de las interfaces lentas de las Smart TVs convencionales, este Apple TV abre Netflix, Disney+ y YouTube al instante en glorioso 4K.<br><br><strong>Ficha Técnica:</strong> Resolución 4K HDR10 y Dolby Vision | Chip A12 Bionic | Siri Remote."},
                    {"id": "lente_tamron_70_200", "titulo": "Lente Tamron SP 70-200mm f/2.8 Di VC USD", "specs": "<strong>Reseña:</strong> Un lente teleobjetivo profesional imprescindible para retratos, deportes y eventos. Su apertura f/2.8 constante produce un desenfoque de fondo (bokeh) cremoso, y su estabilizador VC congela la imagen en condiciones de poca luz.<br><br><strong>Ficha Técnica:</strong> Apertura f/2.8 constante | Estabilizador Óptico VC | Motor de enfoque USD."},
                    {"id": "lente_sigma_17_50", "titulo": "Lente Sigma 17-50mm f/2.8 EX DC OS HSM", "specs": "<strong>Reseña:</strong> El reemplazo perfecto y luminoso para el lente de kit de tu cámara. Ideal para viajes, paisajes y retratos. Es extremadamente nítido de esquina a esquina, incluso con la apertura máxima f/2.8.<br><br><strong>Ficha Técnica:</strong> Rango focal estándar versátil | Estabilizador OS | Motor ultrasónico HSM."},
                    {"id": "impresora_brother", "titulo": "Impresora Láser Brother HL-L2360DW", "specs": "<strong>Reseña:</strong> Famosa por ser un \"tanque de guerra\" que nunca falla. Al ser láser y no de tinta, el tóner no se seca si dejas de imprimir por meses. Además imprime por ambos lados de la hoja automáticamente y vía Wi-Fi desde el celular.<br><br><strong>Ficha Técnica:</strong> Láser Monocromática | 32 ppm | Wi-Fi y Dúplex Automático."},
                    {"id": "maquina_humo", "titulo": "Máquina de Humo 400W", "specs": "<strong>Reseña:</strong> El detalle perfecto para animar cualquier fiesta en casa, evento o sesión de fotos. Calienta rápido y en segundos llena una habitación de un denso humo escénico, realzando cualquier luz de colores o láser.<br><br><strong>Ficha Técnica:</strong> Potencia 400W | Calentamiento en 3 minutos | Disparo continuo con control."}
                ]
            }
        ]
    },
    {
        "categoria": "4. Entrenamiento, Camping & Indumentaria",
        "subcategorias": [
            {
                "nombre": "4.1. Entrenamiento en Casa",
                "items": [
                    {"id": "banca_fullfit", "titulo": "Rack + Banca Reclinable Fullfit con Barra y Discos", "specs": "<strong>Reseña:</strong> El set definitivo para armar tu gimnasio en casa y entrenar todo el cuerpo. Incluye un rack ajustable, ideal para sentadillas seguras o para usarlo como soporte de press. La banca reclinable es sólida y multiposición. Viene lista para usar con su barra y discos pesados de hierro.<br><br><strong>Ficha Técnica:</strong> Incluye: Rack ajustable Fullfit, Banca reclinable, 1 Barra estándar con Pad protector Fullfit y un Set de discos pesados de hierro fundido."},
                    {"id": "remadora_waterrower", "titulo": "Máquina de Remo WaterRower", "specs": "<strong>Reseña:</strong> La máquina de remo definitiva para el hogar. A diferencia de las ruidosas máquinas magnéticas, su resistencia natural a base de agua proporciona un movimiento suave, un sonido relajante y un desafío que se adapta exactamente a la fuerza que le aplicas, brindando una experiencia idéntica a remar en un lago real.<br><br><strong>Ficha Técnica:</strong> Resistencia natural de fluido/agua | Monitor digital de rendimiento integrado (distancia, tiempo, calorías) | Riel de deslizamiento fluido."}
                ]
            },
            {
                "nombre": "4.2. Ropa Outdoor",
                "items": [
                    {"id": "chaqueta_rossignol", "titulo": "Chaqueta Técnica Ski Rossignol Atelier", "specs": "<strong>Reseña:</strong> Indumentaria de gama alta de la colección Atelier Course. Diseñada ergonómicamente para imitar la postura del esquiador. Su membrana de 20K te mantiene totalmente seco frente a ventiscas de nieve o lluvia intensa.<br><br><strong>Ficha Técnica:</strong> Talla: L (EU 50) | Impermeabilidad 20.000mm / Transpirabilidad 20.000g."},
                    {"id": "parka_lippi", "titulo": "Parka Larga Capucha Piel Lippi Thermal", "specs": "<strong>Reseña:</strong> Corte largo muy elegante para el invierno urbano o paseos al sur. Su relleno sintético de tecnología reciclada atrapa el calor corporal excepcionalmente bien, cortando el viento helado gracias a su gorro con piel sintética.<br><br><strong>Ficha Técnica:</strong> Talla: M (Mujer) | Aislamiento térmico reciclado Lippi."},
                    {"id": "pantalon_trangoworld", "titulo": "Pantalón Trekking Trangoworld TRX2", "specs": "<strong>Reseña:</strong> Una armadura para la montaña. Su tejido bielástico Free4Move te da total libertad de movimiento en trepadas rocosas, e incluye refuerzos de Kevlar en los tobillos para evitar cortes con crampones o piedras.<br><br><strong>Ficha Técnica:</strong> Talla: L | Línea técnica TRX2 de alta resistencia a la abrasión."},
                    {"id": "chaqueta_footjoy", "titulo": "Chaqueta Cortaviento Golf FootJoy DryJoys", "specs": "<strong>Reseña:</strong> Favorita entre golfistas profesionales. No solo corta el viento y aguanta la lluvia a la perfección gracias a sus costuras selladas, sino que su diseño súper liviano no restringe el movimiento de los brazos al hacer el swing.<br><br><strong>Ficha Técnica:</strong> Talla: M | Tecnología laminada 100% impermeable extrema."},
                    {"id": "polera_footjoy", "titulo": "Polera Golf Manga Corta FootJoy ProDry", "specs": "<strong>Reseña:</strong> Tela de rendimiento élite que absorbe y evapora el sudor rápidamente. Ideal para jugar golf en verano, cuenta con protección UV bloqueando los rayos dañinos del sol en jornadas al aire libre.<br><br><strong>Ficha Técnica:</strong> Talla: M | Poliéster técnico antimicrobiano (evita olores)."},
                    {"id": "pantalon_naturehike", "titulo": "Pantalón Térmico Pluma Naturehike 800FP", "specs": "<strong>Reseña:</strong> Salvará tus noches acampando bajo cero en la Patagonia o el desierto. Al ser de pluma de ganso de 800 cuins, calienta brutalmente pero se comprime al tamaño de una naranja pequeña en la mochila.<br><br><strong>Ficha Técnica:</strong> Talla: L | 90% Pluma de ganso blanca ultraliviana (800FP)."},
                    {"id": "poleron_tnf", "titulo": "Polerón Fleece The North Face TKA 100", "specs": "<strong>Reseña:</strong> El clásico micropolar de media estación. Es esa capa de abrigo ligera que llevas a todas partes: suave al tacto, muy duradera frente a lavados y fabricada bajo estándares ecológicos reciclados.<br><br><strong>Ficha Técnica:</strong> Talla: L (Hombre) | Microfleece 100% poliéster TKA 100."}
                ]
            },
            {
                "nombre": "4.3. Camping y Climatización",
                "items": [
                    {"id": "aire_kendal", "titulo": "Aire Acondicionado Portátil Kendal 9000 BTU", "specs": "<strong>Reseña:</strong> La salvación para las olas de calor. Al ser portátil, puedes moverlo del living a la pieza. No requiere instalaciones complejas en la pared y su capacidad enfría rápidamente habitaciones estándar de hasta 15-20 m².<br><br><strong>Ficha Técnica:</strong> 9.000 BTU/h | 3 en 1: Frío, Calor y Deshumidificador | Incluye manguera de ventana."},
                    {"id": "cooler_azul_ruedas", "titulo": "Cooler Rígido Ruedas Azul/Blanco 60L", "specs": "<strong>Reseña:</strong> Olvídate de cargar peso en la playa o el asado. Cuenta con un mango telescópico y ruedas grandes para moverlo fácil sobre arena dura o tierra. Su capacidad es gigante, caben varias botellas paradas y hielo de sobra.<br><br><strong>Ficha Técnica:</strong> Capacidad ~60 Litros (~90 Latas) | Ruedas Heavy Duty integradas."},
                    {"id": "cooler_coleman_rojo", "titulo": "Cooler Coleman Performance 48QT Rojo", "specs": "<strong>Reseña:</strong> El icónico cooler de camping americano. Su tecnología ThermOZONE mantiene el hielo hasta 3 días a temperaturas de verano (hasta 32°C). Tiene un tapón inferior a prueba de fugas para vaciar el agua al final del día.<br><br><strong>Ficha Técnica:</strong> Capacidad 45.4 Litros (48 Quarts) | Asas bidireccionales pivotantes."},
                    {"id": "cooler_rubbermaid_blanco", "titulo": "Cooler Rubbermaid Marine Ultra Blanco 45L", "specs": "<strong>Reseña:</strong> Edición Marina, diseñado para aguantar la exposición directa al sol todo el día en lanchas o playas sin que se rompa el plástico (tiene protección UV) y con tornillería resistente a la salinidad.<br><br><strong>Ficha Técnica:</strong> Capacidad ~45 Litros | Inhibidores de radiación solar | Bisagras reforzadas."},
                    {"id": "cooler_klack_azul", "titulo": "Cooler Klack Neveta Portátil Azul 32L", "specs": "<strong>Reseña:</strong> Un cooler térmico intermedio y súper liviano. Ideal para salidas familiares de día completo a parques o excursiones gracias a su núcleo aislante de alta densidad EPS que evita la fuga térmica.<br><br><strong>Ficha Técnica:</strong> Capacidad 32 Litros | Aislamiento en poliestireno expandido de grado alimenticio."}
                ]
            }
        ]
    },
    {
        "categoria": "5. Muebles, Decoración & Artículos del Hogar",
        "subcategorias": [
            {
                "nombre": "5.1. Electrodomésticos",
                "items": [
                    {"id": "lavadora_samsung", "titulo": "Lavadora/Secadora Samsung EcoBubble 15kg/8kg", "specs": "<strong>Reseña:</strong> Una maravilla de la tecnología para el hogar que te ahorra tiempo y esfuerzo. Su sistema EcoBubble penetra las telas para una limpieza profunda incluso en agua fría, cuidando tu ropa. Su motor Digital Inverter garantiza un funcionamiento súper silencioso y de gran durabilidad. Además, cuenta con la increíble función AutoDispense: solo llenas el estanque de detergente una vez y la máquina calcula sola cuánto usar en cada lavado.<br><br><strong>Ficha Técnica:</strong> Capacidad de Lavado: 15 kg | Capacidad de Secado: 8 kg | Panel digital, tecnología EcoBubble y AutoDispense."},
                    {"id": "refrigerador_samsung", "titulo": "Refrigerador Samsung Bottom Freezer Negro Glass", "specs": "<strong>Reseña:</strong> Elegante refrigerador Samsung con acabado de cristal negro que le dará un toque ultra moderno a tu cocina. Su diseño Bottom Freezer (congelador abajo) es súper cómodo para acceder a los alimentos frescos sin agacharte. Cuenta con panel digital exterior y tecnología Digital Inverter que ahorra energía y hace muy poco ruido.<br><br><strong>Ficha Técnica:</strong> Tecnología Digital Inverter | Panel de control táctil exterior | Acabado Black Glass."},
                    {"id": "refrigerador_fdv", "titulo": "Refrigerador FDV Side by Side Black No Frost", "specs": "<strong>Reseña:</strong> Un gigante para familias grandes. Este refrigerador de dos puertas (Side by Side) de la marca FDV destaca por su gran capacidad de almacenamiento y su diseño sofisticado en color negro mate. Cuenta con sistema No Frost para olvidarte de descongelar y paneles digitales independientes para cada lado.<br><br><strong>Ficha Técnica:</strong> Diseño Side by Side (Dos puertas) | Sistema No Frost | Paneles de control de temperatura independientes."},
                    {"id": "horno_oster_airfryer", "titulo": "Horno Eléctrico Oster con Freidora de Aire", "specs": "<strong>Reseña:</strong> Práctico y versátil horno eléctrico Oster que incluye función de freidora de aire (Air Fryer). Perfecto para cocinar tus comidas favoritas de forma más saludable, rápida y crujiente sin usar aceite. Cuenta con perillas de control de tiempo, temperatura y funciones múltiples.<br><br><strong>Ficha Técnica:</strong> Marca: Oster | Funciones: Hornear, Asar, Freír con Aire, Turbo Convección."}
                ]
            },
            {
                "nombre": "5.2. Muebles y Exteriores",
                "items": [
                    {"id": "sillon_cuero_3c", "titulo": "Sofá de Cuero 3 Cuerpos Capitoné", "specs": "<strong>Reseña:</strong> Elegante y robusto sofá de cuero de tres cuerpos con diseño capitoné en el respaldo y asiento. Ideal para darle un toque clásico y sofisticado a tu living o sala de estar. Su estructura sólida y tapiz de alta durabilidad aseguran años de comodidad.<br><br><strong>Ficha Técnica:</strong> Capacidad: 3 cuerpos | Material: Tapiz de cuero | Diseño: Capitoné."},
                    {"id": "sitial_cuero", "titulo": "Sitial / Sillón Individual de Cuero", "specs": "<strong>Reseña:</strong> Cómodo sitial de cuero individual que hace juego perfecto con el sofá principal. Su diseño de líneas rectas y asiento capitoné lo convierten en el complemento ideal para rincones de lectura o como asiento extra en el living.<br><br><strong>Ficha Técnica:</strong> Capacidad: 1 cuerpo | Material: Tapiz de cuero | Diseño: Capitoné."},
                    {"id": "sillon_milk", "titulo": "Sofá Seccional en L Tienda Milk (Fundas Lavables)", "specs": "<strong>Reseña:</strong> El sofá definitivo para relajarse en familia. De la reconocida tienda de diseño Milk, este amplio seccional destaca por su máxima comodidad, profundidad y estética limpia en tono crudo. Lo mejor: todas sus fundas son 100% desmontables y lavables en lavadora, ideal para un mantenimiento fácil e impecable.<br><br><strong>Ficha Técnica:</strong> Formato: Seccional en L | Tapicería: Fundas desmontables y lavables | Origen: Tienda Milk."},
                    {"id": "comedor_vidrio_madera", "titulo": "Mesa de Comedor Vidrio y Madera Amoblé (240x140 cm)", "specs": "<strong>Reseña:</strong> Una mesa de comedor imponente y de diseño arquitectónico espectacular. Cuenta con una cubierta de cristal templado de gran grosor y formato extra grande (2,4 metros), ideal para 10-12 personas. Su base es una verdadera escultura que combina cristal estructural con un macizo bloque de madera noble.<br><br><strong>Ficha Técnica:</strong> Dimensiones: 240 cm de largo x 140 cm de ancho | Materiales: Cristal templado y madera maciza | Estilo Amoblé."},
                    {"id": "porton_madera", "titulo": "Portón Doble Tallado Madera Maciza", "specs": "<strong>Reseña:</strong> Pieza arquitectónica única, estilo colonial o campestre. Ideal para darle un toque imponente a la entrada principal de un fundo, parcela, o para usarla como una puerta decorativa majestuosa en proyectos de interiorismo.<br><br><strong>Ficha Técnica:</strong> Madera maciza pesada (noble) | Apliques metálicos forjados a mano de época."},
                    {"id": "rampa_moto", "titulo": "Rampa Aluminio Plegable Moto/ATV", "specs": "<strong>Reseña:</strong> Carga tu moto de enduro, cuatrimoto o cortacésped a tu camioneta en segundos, tú solo y sin esfuerzo. Como es de aluminio no se oxida, es sorprendentemente liviana para cargar, y se dobla por la mitad para guardarla fácil.<br><br><strong>Ficha Técnica:</strong> Aluminio 6061 ultra liviano (~7.2 kg) | Soporta hasta 340 kg de carga segura."},
                    {"id": "espejo_textil", "titulo": "Espejo Artesanal Marco Textil Ovalado", "specs": "<strong>Reseña:</strong> Detalles que le dan alma a los espacios. Este espejo presenta un marco con tapicería artesanal estilo patchwork indio/boho, perfecto para sumar textura y colores cálidos a una entrada, dormitorio o sala de estar.<br><br><strong>Ficha Técnica:</strong> Formato ovalado de pared | Marco ancho de tapizado artesanal con bordados a mano."}
                ]
            }
        ]
    }
]

# =========================================================
# 🟡 INTEGRACIÓN DEFINITIVA DE MODIFICACIONES DEL ADMIN
# =========================================================
mods_guardadas = {}
vendidos_guardados = {}

if os.path.exists("configuracion_garage.json"):
    try:
        with open("configuracion_garage.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            mods_guardadas = data.get("modificaciones", {})
            vendidos_guardados = data.get("estados_vendido", {})
    except Exception:
        pass

if os.path.exists("nuevas_fotos_asignadas.json"):
    try:
        with open("nuevas_fotos_asignadas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict) and "modificaciones" not in data:
                for k, v in data.items():
                    if isinstance(v, list) and k not in mods_guardadas:
                        asignaciones[k] = v
    except Exception:
        pass

for cat in catalogo:
    for subcat in cat["subcategorias"]:
        for item in subcat["items"]:
            item_id = item["id"]
            if item_id in mods_guardadas:
                item["titulo"] = mods_guardadas[item_id].get("titulo", item["titulo"])
                item["specs"] = mods_guardadas[item_id].get("specs", item["specs"])
                precios_definidos[item_id] = mods_guardadas[item_id].get("precio", precios_definidos.get(item_id, 50000))
                asignaciones[item_id] = mods_guardadas[item_id].get("fotos", asignaciones.get(item_id, []))

flat_products = []
for cat in catalogo:
    for subcat in cat["subcategorias"]:
        for item in subcat["items"]:
            precio_admin = precios_definidos.get(item["id"], 50000)
            try:
                precio_admin = int(precio_admin)
            except (TypeError, ValueError):
                precio_admin = 0

            flat_products.append({
                "id": item["id"],
                "titulo": item["titulo"],
                "specs": item["specs"],
                "precioInicial": precio_admin,
                "fotos": asignaciones.get(item["id"], [])
            })

# =========================================================
# 🔵 GENERACIÓN DE INDEX.HTML (PÚBLICO)
# =========================================================
html_publico_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo Oficial de Venta de Garage</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
        body { font-family: 'Plus Jakarta Sans', sans-serif; margin: 0; padding: 20px 10px 100px 10px; background-color: #fcf8f5; color: #2c221e; }
        
        .header-container { text-align: center; max-width: 900px; margin: 0 auto 20px auto; padding: 25px 15px; background: #ffffff; border-radius: 20px; box-shadow: 0 4px 20px rgba(184, 137, 107, 0.08); border: 1px solid #f2e6df; }
        h1 { color: #8c4327; font-size: 28px; margin: 0 0 10px 0; font-weight: 700; }
        .subtitle { color: #7a685d; font-size: 14px; margin-bottom: 20px; }
        
        .rules-card { background: #fff8f5; border: 1px solid #e6b8a2; padding: 20px; border-radius: 14px; max-width: 900px; margin: 0 auto 25px auto; text-align: left; }
        .rules-card h3 { margin-top: 0; color: #8c4327; font-size: 18px; margin-bottom: 12px; }
        .rules-card ul { margin: 0; padding-left: 20px; color: #61463a; font-size: 14px; line-height: 1.6; }
        
        .user-form-card { background: #faf0eb; border: 2px solid #e6b8a2; padding: 20px; border-radius: 14px; max-width: 900px; margin: 0 auto; text-align: left; box-sizing: border-box;}
        .form-grid { display: grid; grid-template-columns: 1fr; gap: 12px; }
        .form-group label { display: block; font-size: 13px; font-weight: 700; color: #8c4327; margin-bottom: 6px; }
        .form-group input[type="text"], .form-group input[type="email"] { width: 92%; padding: 10px; border: 1px solid #d4a38d; border-radius: 8px; font-size: 15px; background: #ffffff; outline: none; }
        .checkbox-container { display: flex; align-items: center; gap: 10px; background: #ffffff; padding: 12px; border: 1px solid #d4a38d; border-radius: 8px; cursor: pointer;}
        .checkbox-container input { width: 20px; height: 20px; cursor: pointer; }
        .checkbox-container span { font-size: 15px; font-weight: 600; color: #2c221e; }
        
        /* ESTILOS DEL BUSCADOR */
        .search-box:focus { border-color: #8c4327 !important; box-shadow: 0 0 8px rgba(140, 67, 39, 0.2); }
        .hidden-by-search { display: none !important; }
        
        .cat-title { background: linear-gradient(135deg, #8c4327 0%, #a65333 100%); color: #ffffff; padding: 12px 18px; margin: 30px auto 15px auto; max-width: 900px; border-radius: 12px; font-size: 18px; }
        .subcat-title { color: #a65333; max-width: 900px; margin: 20px auto 10px auto; border-bottom: 2px solid #ecdcd3; padding-bottom: 6px; font-size: 16px; }
        
        .item-card { display: flex; flex-direction: column; max-width: 900px; margin: 0 auto 20px auto; background: #ffffff; border-radius: 16px; padding: 20px; border: 1px solid #f2e6df; gap: 15px; box-shadow: 0 2px 10px rgba(184, 137, 107, 0.05); transition: opacity 0.3s;}
        .item-title { font-size: 18px; font-weight: 700; margin-bottom: 8px; line-height:1.2; }
        .specs-box { background-color: #faf0eb; border-left: 4px solid #d47a59; padding: 12px 16px; border-radius: 6px; margin-bottom: 12px; font-size: 13px; color: #4e352b; line-height: 1.5; }
        .price-badge { display: inline-block; background-color: #8c4327; color: #ffffff; padding: 6px 12px; border-radius: 8px; font-weight: 700; font-size: 15px; margin-bottom: 10px; }
        
        .gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: 10px; }
        .gallery img { width: 100%; height: 120px; object-fit: cover; border-radius: 8px; border: 1px solid #e8dad1; cursor: pointer; transition: 0.2s; }
        .gallery img:hover { filter: brightness(0.9); }
        
        .offer-box { width: 100%; border: 2px dashed #e6b8a2; border-radius: 12px; padding: 15px; background: #fff8f5; box-sizing: border-box; text-align: center; }
        .offer-input-group input { width: 80%; padding: 10px; border: 1px solid #d4a38d; border-radius: 6px; text-align: center; font-size: 16px; font-weight: 700; margin-bottom:10px; }
        .btn-add { background: #1e3a8a; color: #ffffff; border: none; padding: 10px 15px; border-radius: 8px; font-size: 14px; font-weight: 700; cursor: pointer; width: 90%; transition: 0.2s; }
        
        /* BARRA FLOTANTE */
        .cart-bar { display: none; position: fixed; bottom: 0; left: 0; width: 100%; background: #ffffff; border-top: 2px solid #e2e8f0; padding: 15px 0; text-align: center; z-index: 1000; box-shadow: 0 -4px 15px rgba(0,0,0,0.1); }
        .cart-text { font-size: 15px; font-weight: 700; color: #1e293b; margin-bottom: 10px; }
        .btn-whatsapp { background: #25D366; color: white; border: none; padding: 12px 25px; border-radius: 30px; font-size: 16px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; transition: 0.2s; }
        .btn-whatsapp:disabled { opacity: 0.7; cursor: not-allowed; }
        
        /* MODAL IMÁGENES */
        .modal { display: none; position: fixed; z-index: 9999; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.9); justify-content: center; align-items: center; cursor: zoom-out; }
        .modal img { max-width: 95%; max-height: 90%; border-radius: 8px; object-fit: contain; }

        @media(min-width: 768px) {
            .item-card { flex-direction: row; padding: 25px; }
            .item-left { flex: 1; padding-right: 20px; }
            .offer-box { width: 260px; margin-top:0; }
            .form-grid { grid-template-columns: 1fr 1fr; }
            .user-form-card .form-group:last-child { grid-column: span 2; }
        }
    </style>
</head>
<body>
    <div class="header-container">
        <h1>Catálogo de Venta de Garage</h1>
        <div class="subtitle">Santiago, Chile | Agrega tus ofertas a cada producto y envíalas juntas por WhatsApp.</div>
    </div>

    <!-- REGLAS DEL JUEGO -->
    <div class="rules-card">
        <h3>📌 Reglas y Formato de Compra</h3>
        <ul>
            <li><strong>¿Cómo comprar?</strong> Agrega el valor que ofreces por cada producto que te interese y haz clic en "Guardar en Carrito". Al final, envía todo tu carrito junto usando el botón verde de abajo.</li>
            <li><strong>Cierre de Ofertas:</strong> Se recibirán ofertas hasta una fecha específica (por definirse). ¡Asegura tus productos antes de que se agoten!</li>
            <li><strong>Muestra y Retiro de productos:</strong> La entrega y muestra de los artículos se realiza en la <strong>comuna de Lo Barnechea (sector Colegio Everest)</strong>. El horario y los detalles se coordinan directamente vía WhatsApp. Todo se entrega probado y en su estado actual.</li>
            <li><strong>¿No tienes cómo llevarlo?</strong> Marca la casilla de despacho al llenar tus datos y te lo enviamos por un costo fijo de $50.000.</li>
        </ul>
    </div>

    <div class="user-form-card">
        <div style="font-weight: 700; color: #8c4327; margin-bottom: 15px;">👤 Ingresa tus datos antes de ofertar</div>
        <div class="form-grid">
            <div class="form-group"><label>Tu Nombre y Apellido *</label><input type="text" id="userName" placeholder="Ej: Juan Pérez"></div>
            <div class="form-group"><label>Teléfono / WhatsApp *</label><input type="text" id="userPhone" placeholder="+56 9..."></div>
            <div class="form-group"><label>Correo Electrónico</label><input type="email" id="userEmail" placeholder="juan@gmail.com"></div>
            
            <div class="form-group">
                <label class="checkbox-container">
                    <input type="checkbox" id="userDespacho" onchange="actualizarCarrito()">
                    <span>🚚 Necesito despacho a domicilio (+$50.000 CLP)</span>
                </label>
            </div>
        </div>
    </div>
    
    <div style="max-width: 900px; margin: 30px auto 10px auto; text-align: center;">
        <input type="text" id="searchInput" class="search-box" onkeyup="filtrarProductos()" placeholder="🔍 Buscar por producto, marca o categoría..." style="width: 90%; max-width: 600px; padding: 14px 20px; font-size: 16px; border: 2px solid #e6b8a2; border-radius: 30px; outline: none; transition: 0.3s; color:#2c221e;">
    </div>

__PRODUCTOS_HTML__

    <div id="cart-bar" class="cart-bar">
        <div class="cart-text">🛒 <span id="cart-count">0</span> ofertas acumuladas (Total: $<span id="cart-total">0</span> CLP) <span id="cart-envio-text" style="color:#e11d48; font-size:13px; display:none;">(Incluye Despacho)</span></div>
        <button class="btn-whatsapp" onclick="enviarFormularioFinal()">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.98 1.005-3.645-.235-.373a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.882-9.882 9.882m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            Enviar Oferta por WhatsApp
        </button>
    </div>

    <!-- MODAL PARA IMAGENES -->
    <div id="imageModal" class="modal" onclick="cerrarImagen()">
        <img id="modalImg" src="">
    </div>

    <script>
        let carrito = {};

        // SISTEMA DE PLEGADO DE CATEGORÍAS
        document.addEventListener("DOMContentLoaded", function() {
            let contents = document.querySelectorAll('.category-content');
            let icons = document.querySelectorAll('.cat-icon');
            // Plegar todas excepto la primera al cargar la página
            contents.forEach((content, index) => {
                if(index !== 0) {
                    content.style.display = 'none';
                    icons[index].innerText = '▶';
                }
            });
        });

        function toggleCategoria(idx) {
            let content = document.getElementById('cat-content-' + idx);
            let icon = document.getElementById('cat-icon-' + idx);
            if (content.style.display === 'none' || content.style.display === '') {
                content.style.display = 'block';
                icon.innerText = '▼';
            } else {
                content.style.display = 'none';
                icon.innerText = '▶';
            }
        }

        // SISTEMA DE BÚSQUEDA INTELIGENTE
        function filtrarProductos() {
            let input = document.getElementById('searchInput').value.toLowerCase();
            let catSections = document.querySelectorAll('.category-section');
            
            catSections.forEach((section) => {
                let items = section.querySelectorAll('.item-card');
                let catHasVisibleItems = false;
                
                items.forEach(card => {
                    let text = card.innerText.toLowerCase();
                    if (text.includes(input)) {
                        card.classList.remove('hidden-by-search');
                        catHasVisibleItems = true;
                    } else {
                        card.classList.add('hidden-by-search');
                    }
                });
                
                let subcats = section.querySelectorAll('.subcat-section');
                subcats.forEach(sub => {
                    let visibleItems = sub.querySelectorAll('.item-card:not(.hidden-by-search)');
                    if (visibleItems.length > 0) {
                        sub.style.display = 'block';
                    } else {
                        sub.style.display = 'none';
                    }
                });

                let content = section.querySelector('.category-content');
                let icon = section.querySelector('.cat-icon');
                
                if (input.trim() !== '') {
                    // Si se está buscando algo, se abren automáticamente las carpetas que coincidan
                    if (catHasVisibleItems) {
                        section.style.display = 'block';
                        content.style.display = 'block';
                        icon.innerText = '▼';
                    } else {
                        section.style.display = 'none';
                    }
                } else {
                    // Si se borra la búsqueda, mostrar las categorías de nuevo
                    section.style.display = 'block';
                }
            });
        }

        // SISTEMA DEL CARRITO Y FORMULARIO
        function agregarOferta(id) {
            let titulo = document.getElementById('title-' + id).innerText;
            let input = document.getElementById('input-offer-' + id);
            let monto = parseInt(input.value);

            if (isNaN(monto) || monto <= 0) { alert("Ingresa un monto válido."); return; }

            carrito[id] = { titulo: titulo, monto: monto };
            
            let btn = document.getElementById('btn-add-' + id);
            btn.innerHTML = "✅ Guardado ($" + monto.toLocaleString('es-CL') + ")";
            btn.style.background = "#15803d";
            actualizarCarrito();
        }

        function actualizarCarrito() {
            let count = Object.keys(carrito).length;
            let total = Object.values(carrito).reduce((acc, curr) => acc + curr.monto, 0);
            
            let necesitaDespacho = document.getElementById('userDespacho').checked;
            if (necesitaDespacho && count > 0) {
                total += 50000;
                document.getElementById('cart-envio-text').style.display = 'inline';
            } else {
                document.getElementById('cart-envio-text').style.display = 'none';
            }
            
            let bar = document.getElementById('cart-bar');
            if (count > 0) {
                bar.style.display = 'block';
                document.getElementById('cart-count').innerText = count;
                document.getElementById('cart-total').innerText = total.toLocaleString('es-CL');
            } else {
                bar.style.display = 'none';
            }
        }

        function enviarFormularioFinal() {
            let nombre = document.getElementById('userName').value.trim();
            let telefono = document.getElementById('userPhone').value.trim();
            let email = document.getElementById('userEmail').value.trim();
            let necesitaDespacho = document.getElementById('userDespacho').checked;

            if (Object.keys(carrito).length === 0) {
                alert("No has agregado ninguna oferta. Ingresa un monto y presiona 'Guardar en Carrito' en algún producto.");
                return;
            }

            if (!nombre || !telefono) {
                alert("Por favor, ingresa tu Nombre y Teléfono en la parte superior antes de enviar.");
                window.scrollTo({ top: 0, behavior: 'smooth' });
                return;
            }

            let btnWhatsapp = document.querySelector('.btn-whatsapp');
            let textoOriginal = btnWhatsapp.innerHTML;
            btnWhatsapp.innerHTML = "⏳ Registrando oferta...";
            btnWhatsapp.style.background = "#64748b";
            btnWhatsapp.disabled = true;

            let items = Object.values(carrito);
            let total = 0;
            let detalleStr = "";
            let msjWhatsApp = `Hola Benjamín, soy *${nombre}*.\\n\\nTe quiero hacer la siguiente oferta:\\n\\n`;

            items.forEach(i => {
                let valStr = i.monto.toLocaleString('es-CL');
                detalleStr += `- ${i.titulo} ($${valStr} CLP)\\n`;
                msjWhatsApp += `📦 *${i.titulo}*\\n💰 Ofrezco: $${valStr} CLP\\n\\n`;
                total += i.monto;
            });

            if (necesitaDespacho) {
                detalleStr += `- Despacho a Domicilio ($50.000 CLP)\\n`;
                msjWhatsApp += `🚚 *Despacho a Domicilio* (+ $50.000 CLP)\\n\\n`;
                total += 50000;
            }

            let totalStr = total.toLocaleString('es-CL');
            msjWhatsApp += `*TOTAL FINAL: $${totalStr} CLP*\\n\\n¿Te parece bien?`;
            
            let urlAppScript = "[LINK_GOOGLE_APPS_SCRIPT]";
            let dataGoogle = {
                nombre: nombre,
                telefono: telefono,
                email: email,
                detalleStr: detalleStr,
                totalStr: totalStr
            };

            let urlWhatsApp = `https://api.whatsapp.com/send?phone=[NUMERO_WHATSAPP]&text=${encodeURIComponent(msjWhatsApp)}`;

            if(urlAppScript !== "PEGAR_AQUI_LA_URL_DE_GOOGLE") {
                fetch(urlAppScript, {
                    method: 'POST',
                    mode: 'no-cors',
                    body: JSON.stringify(dataGoogle)
                }).catch(e => console.log(e));
            }

            setTimeout(function() {
                window.location.href = urlWhatsApp;
                btnWhatsapp.innerHTML = textoOriginal;
                btnWhatsapp.style.background = "#25D366";
                btnWhatsapp.disabled = false;
            }, 1500);
        }

        function ampliarImagen(src) {
            document.getElementById('modalImg').src = src;
            document.getElementById('imageModal').style.display = 'flex';
        }
        function cerrarImagen() { document.getElementById('imageModal').style.display = 'none'; }
    </script>
</body>
</html>
"""

productos_html = ""
for cat_idx, cat in enumerate(catalogo):
    productos_html += f'<div class="category-section" id="cat-section-{cat_idx}">\n'
    productos_html += f'<h2 class="cat-title" onclick="toggleCategoria({cat_idx})" style="cursor:pointer; display:flex; justify-content:space-between; align-items:center;"><span>{cat["categoria"]}</span> <span class="cat-icon" id="cat-icon-{cat_idx}">▼</span></h2>\n'
    productos_html += f'<div class="category-content" id="cat-content-{cat_idx}">\n'
    
    for subcat in cat["subcategorias"]:
        productos_html += f'<div class="subcat-section">\n'
        productos_html += f'<h3 class="subcat-title">{subcat["nombre"]}</h3>\n'
        for item in subcat["items"]:
            precio_raw = precios_definidos.get(item["id"], 50000)
            
            try:
                precio_def = int(precio_raw)
            except (TypeError, ValueError):
                precio_def = 0
                
            fotos_item = asignaciones.get(item["id"], [])
            
            is_vendido = item["id"] in vendidos_guardados and vendidos_guardados[item["id"]] == "vendido"
            
            opacity_style = "opacity: 0.6;" if is_vendido else ""
            badge_html = f'<div class="price-badge" id="badge-{item["id"]}" style="background: #475569;">⛔ VENDIDO</div>' if is_vendido else f'<div class="price-badge" id="badge-{item["id"]}">Precio Sugerido: ${precio_def:,} CLP</div>'
            
            offer_box_html = f'''
                <div class="offer-box" id="offer-box-{item['id']}" style="background: #f1f5f9; border: 2px solid #cbd5e1;">
                    <h3 style="color:#475569; margin:0;">Este producto ya fue vendido</h3>
                </div>
            ''' if is_vendido else f'''
                <div class="offer-box" id="offer-box-{item['id']}">
                    <div style="font-size:14px; font-weight:bold; color:#8c4327; margin-bottom:10px;">Tu Oferta ($ CLP):</div>
                    <div class="offer-input-group"><input type="number" id="input-offer-{item['id']}" placeholder="$ 0"></div>
                    <button class="btn-add" id="btn-add-{item['id']}" onclick="agregarOferta('{item['id']}')">🛒 Guardar en Carrito</button>
                </div>
            '''

            productos_html += f'''
            <div class="item-card" id="card-{item['id']}" style="{opacity_style}">
                <div class="item-left">
                    <div class="item-title" id="title-{item['id']}">{item["titulo"]}</div>
                    {badge_html}
                    <div class="specs-box" id="specs-{item['id']}">{item.get("specs", "")}</div>
                    <div class="gallery">
            '''
            for img in fotos_item:
                productos_html += f'<img src="{img}" alt="{item["titulo"]}" loading="lazy" onclick="ampliarImagen(this.src)">\n'
            
            productos_html += f'''
                    </div>
                </div>
                {offer_box_html}
            </div>
            '''
        productos_html += f'</div>\n' # Cierre de subcat-section
    productos_html += f'</div>\n</div>\n' # Cierre de category-content y category-section

html_publico = html_publico_template.replace("__PRODUCTOS_HTML__", productos_html)
html_publico = html_publico.replace("[NUMERO_WHATSAPP]", NUMERO_WHATSAPP)
html_publico = html_publico.replace("[LINK_GOOGLE_APPS_SCRIPT]", LINK_GOOGLE_APPS_SCRIPT)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_publico)


# =========================================================
# 🟠 GENERACIÓN DE PANEL ADMIN CON ACCESO A GOOGLE SHEETS
# =========================================================
html_admin_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Panel Súper Administrador - Venta Garage</title>
    <style>
        body { font-family: sans-serif; background: #f8fafc; padding: 20px; }
        .card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); max-width: 1200px; margin: 0 auto; }
        .header-box { background: #eff6ff; padding: 15px; border-radius: 8px; border: 1px solid #bfdbfe; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px;}
        th, td { padding: 10px; border-bottom: 1px solid #ccc; text-align: left; vertical-align: top; }
        th { background: #e2e8f0; color: #1e293b; }
        input[type="text"], input[type="number"] { width: 95%; padding: 6px; box-sizing: border-box; border: 1px solid #94a3b8; border-radius: 4px; }
        textarea { width: 95%; box-sizing: border-box; padding: 6px; border: 1px solid #94a3b8; border-radius: 4px; font-family: sans-serif; font-size: 13px;}
        button { border: none; padding: 8px 12px; border-radius: 6px; font-weight: bold; color: white; cursor: pointer; transition: 0.2s;}
        .btn-vendido { background: #ef4444; }
        .btn-disponible { background: #10b981; }
        .btn-guardar { background: #2563eb; margin-top: 10px; }
        .btn-guardar:hover { background: #1d4ed8; }
        .btn-descargar { background: #8b5cf6; padding: 12px 20px; font-size: 15px; }
        .btn-descargar:hover { background: #7c3aed; }
    </style>
</head>
<body>
    <div class="card" style="margin-bottom: 20px; text-align: center; border-left: 5px solid #10b981;">
        <h2 style="margin-top:0; color:#1e3a8a;">📊 Ver Ofertas Recibidas</h2>
        <p>Todas las ofertas que envíen tus clientes se están guardando automáticamente en tu Google Sheets.</p>
        <a href="https://docs.google.com/spreadsheets/" target="_blank" style="display:inline-block; background: #10b981; color: white; padding: 12px 20px; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 16px;">Abrir mi Google Sheets</a>
    </div>

    <div class="card">
        <h1 style="color:#1e3a8a; margin-top:0;">⚙️ Panel Central de Administración</h1>
        
        <div class="header-box">
            <h3 style="margin-top:0; color:#1e3a8a;">📥 Guardar Modificaciones Completas</h2>
            <p style="font-size:14px; color:#334155;">Para aplicar tus cambios en la web pública de forma permanente:</p>
            <ol style="font-size:14px; color:#334155;">
                <li>Edita títulos, descripciones, precios, fotos o marca como "Vendido".</li>
                <li>Haz clic en "Guardar Cambios" en cada fila que modifiques.</li>
                <li>Haz clic en el botón morado para descargar <strong>configuracion_garage.json</strong>.</li>
                <li>Guarda ese archivo en la carpeta de Python y vuelve a correr tu script.</li>
            </ol>
            <button class="btn-descargar" onclick="descargarConfiguracionJSON()">⬇️ Descargar Configuración Completa (JSON)</button>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th style="width:10%">ID / Estado</th>
                    <th style="width:15%">Título</th>
                    <th style="width:25%">Descripción (Admite HTML)</th>
                    <th style="width:10%">Precio ($)</th>
                    <th style="width:25%">📸 Asignar Fotos</th>
                    <th style="width:15%">Acciones</th>
                </tr>
            </thead>
            <tbody id="tbody"></tbody>
        </table>
    </div>
    
    <script>
        let catalogoAdmin = __CATALOGO_JSON__;
        
        let estados_venta = JSON.parse(localStorage.getItem('estados_garage_vendido')) || {};
        let mods = JSON.parse(localStorage.getItem('modificaciones_garage')) || {};

        function renderTable() {
            let tbody = document.getElementById('tbody');
            tbody.innerHTML = "";
            
            catalogoAdmin.forEach(item => {
                let isVendido = estados_venta[item.id] === 'vendido';
                
                let t = mods[item.id] ? mods[item.id].titulo : item.titulo;
                let s = mods[item.id] ? mods[item.id].specs : item.specs;
                let p = mods[item.id] ? mods[item.id].precio : item.precioInicial;
                let f = mods[item.id] && mods[item.id].fotos ? mods[item.id].fotos : item.fotos;
                
                let textEstado = isVendido ? "<span style='color:#ef4444; font-weight:bold;'>Vendido</span>" : "<span style='color:#10b981; font-weight:bold;'>Disponible</span>";
                let btnEstado = isVendido 
                    ? `<button class="btn-disponible" onclick="toggleVendido('${item.id}', false)" style="width:100%;">🔄 Volver a Disponible</button>` 
                    : `<button class="btn-vendido" onclick="toggleVendido('${item.id}', true)" style="width:100%;">⛔ Marcar como Vendido</button>`;
                
                let tr = document.createElement('tr');
                if(isVendido) tr.style.background = "#f1f5f9";
                
                tr.innerHTML = `
                    <td>
                        <small style="color:#64748b;">${item.id}</small><br><br>${textEstado}
                    </td>
                    <td><input type="text" id="t-${item.id}" value="${t.replace(/"/g, '&quot;')}"></td>
                    <td><textarea id="s-${item.id}" rows="5">${s}</textarea></td>
                    <td><input type="number" id="p-${item.id}" value="${p}"></td>
                    <td>
                        <p style="font-size:11px; color:#64748b; margin:0 0 5px 0;">*(Elegir fotos para extraer sus nombres)*</p>
                        <input type="file" multiple accept="image/*" onchange="extraerNombresFotos(event, '${item.id}')" style="font-size:11px; margin-bottom:5px;">
                        <textarea id="ft-${item.id}" rows="3" style="font-size:11px;" placeholder="Ej: foto1.jpg, foto2.jpg">${f.join(', ')}</textarea>
                    </td>
                    <td>
                        ${btnEstado}
                        <button class="btn-guardar" onclick="guardarMods('${item.id}')" style="width:100%;">💾 Guardar Cambios</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function extraerNombresFotos(event, id) {
            let files = event.target.files;
            if(files.length > 0) {
                let fileNames = Array.from(files).map(file => file.name);
                document.getElementById('ft-' + id).value = fileNames.join(', ');
            }
        }

        function toggleVendido(id, vender) {
            if(vender) estados_venta[id] = 'vendido';
            else delete estados_venta[id];
            localStorage.setItem('estados_garage_vendido', JSON.stringify(estados_venta));
            renderTable();
        }

        function guardarMods(id) {
            let stringFotos = document.getElementById('ft-'+id).value;
            let arrayFotos = stringFotos.split(',').map(s => s.trim()).filter(s => s !== "");

            mods[id] = {
                titulo: document.getElementById('t-'+id).value,
                specs: document.getElementById('s-'+id).value,
                precio: parseInt(document.getElementById('p-'+id).value),
                fotos: arrayFotos
            };
            localStorage.setItem('modificaciones_garage', JSON.stringify(mods));
            
            let btn = event.target;
            let textoOriginal = btn.innerText;
            btn.innerText = "¡Guardado!";
            btn.style.background = "#10b981";
            setTimeout(() => {
                btn.innerText = textoOriginal;
                btn.style.background = "#2563eb";
            }, 1500);
        }

        function descargarConfiguracionJSON() {
            let exportData = {
                modificaciones: mods,
                estados_vendido: estados_venta
            };
            
            let dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(exportData, null, 2));
            let downloadAnchorNode = document.createElement('a');
            downloadAnchorNode.setAttribute("href", dataStr);
            downloadAnchorNode.setAttribute("download", "configuracion_garage.json");
            document.body.appendChild(downloadAnchorNode);
            downloadAnchorNode.click();
            downloadAnchorNode.remove();
        }

        document.addEventListener("DOMContentLoaded", renderTable);
    </script>
</body>
</html>
"""

html_admin = html_admin_template.replace('__CATALOGO_JSON__', json.dumps(flat_products))

with open("Panel_Administrador_Ofertas.html", "w", encoding="utf-8") as f:
    f.write(html_admin)

print("¡Archivos generados exitosamente!")
print("✅ Catálogo actualizado con el Horno Oster, Sofá y Sitial de cuero.")
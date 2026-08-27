# STYLE: motion-design

Estética padrão do Trilho A. Substitui a colagem de papel do prompt original.

Referência mental: gráfico explicativo de veículo editorial sério (Vox, Bloomberg
Originals, Kurzgesagt sem os personagens). Vetor plano, geometria limpa, tipografia
como elemento de composição, muito espaço negativo.

---

## Regras de composição (valem para todo beat)

1. **Um elemento herói** dominando cerca de 70 por cento do peso visual.
2. **No máximo 2 a 3 elementos de apoio.** Mais que isso morre em tela de celular.
3. **Espaço negativo generoso.** O vazio é parte do design, não sobra.
4. **Texto só quando o beat carrega data, número ou nome.** Um rótulo, de 1 a 4
   palavras, em sans condensada. Fora isso, zero texto.
5. **Um foco claro.** Se o olho não sabe onde pousar em meio segundo, refaz.
6. **Nunca ilustrar a frase inteira.** Encontrar a ideia central e desenhar só ela.

## Vocabulário visual preferido

Objeto isolado, documento, formulário, calendário, cronômetro, mapa, planta baixa,
gráfico de barra, linha do tempo, recibo, chave, porta, janela, medidor, etiqueta de
preço, carimbo, pasta, checklist. Figura humana só como silhueta geométrica abstrata,
sem rosto, e apenas quando indispensável.

## Uso de cor

Paleta dos tokens em `brand/DNA.md`. `SIGNAL` só entra quando a narração fala de
custo, risco ou prazo. Se `SIGNAL` aparece em todo beat, ele deixa de significar
alguma coisa.

---

## STYLE BLOCK (incluir literalmente em todo image prompt)

> premium editorial motion design frame, flat vector illustration with subtle
> dimensional depth, clean geometric construction and precise consistent stroke
> weights, generous negative space, one dominant hero element holding roughly seventy
> percent of visual weight, soft long shadows cast at a consistent forty five degree
> angle, restrained palette of warm off-white paper base (#F4F1EC), deep ink navy
> (#16202B), and cool slate gray (#64748B), with one saturated teal accent (#12A594)
> and a warm amber secondary (#F5A524), a single hot red signal accent (#E5484D) used
> only where cost or risk or deadline is implied, condensed geometric sans-serif
> lettering only where a label is specified, faint paper grain and a very soft
> vignette, matte finish, flat even diffused lighting, calm confident editorial tone

## CLOSER (encerrar todo image prompt exatamente assim)

> Every element must read as precise vector motion design: clean geometry, consistent
> stroke weights, flat fills with restrained soft shadow, generous negative space, and
> a single unmistakable focal point. NOT photorealistic, NOT 3D render, NOT hand-drawn
> sketch, NOT cartoon mascot, NOT infographic clutter, no heavy gradients, no busy
> background, no watermark, no logos, no text beyond the specified label. Premium
> editorial motion design aesthetic, {RATIO}, ultra-detailed, 8K.

`{RATIO}` é substituído pelo valor da execução (padrão `9:16`).

---

## UNIVERSAL VIDEO PROMPT (motion design)

Aplicado a toda imagem gerada. Sai uma vez, íntegro, no STATE 8.

> Transform the provided image into a 6-second premium editorial motion design
> animation. Preserve the final composition of the provided image exactly. Do not
> redesign, reposition, resize, recolor, or replace any element. The provided image is
> the FINISHED frame that the animation builds toward.
>
> Style: precise vector motion design in motion. Flat geometric shapes with consistent
> stroke weights, clean fills, soft long shadows, faint paper grain. Every element
> animates as a rigid vector object with crisp edges. Snappy confident easing, custom
> ease-out curves, slight overshoot and settle on arrival, staggered timing between
> elements of roughly 3 to 5 frames. Never sluggish, never bouncy-cartoon, never
> smooth-CGI-organic.
>
> CAMERA, STRICT: the camera stays completely locked for the entire clip. No zoom, no
> pan, no tilt, no rotation, no orbit, no dolly, no tracking, no handheld shake, no
> focus pulls, no reframing, no cuts, no transitions, no morphing, no object
> replacement, no time skips. One continuous static shot.
>
> 0 TO 4 SECONDS, STAGGERED BUILD: the frame opens on the EMPTY background plate only:
> the bare base color with its grain and vignette and any fixed scaffolding (a grid, a
> baseline, a frame edge), with every story element absent. Elements then enter one by
> one, back to front, in narrative order. Background shapes fade and scale up from
> ninety-six percent. The hero element slides in along a single axis and settles with a
> small overshoot. Supporting elements stagger in after it. Lines and connectors draw
> themselves along their own path. Shadows grow as their owners arrive. Any specified
> label types on or wipes in last, character group by character group. Each arrival
> lands cleanly and casts its correct shadow. No element moves again after it lands. By
> 4 seconds the frame exactly matches the provided image.
>
> 4 TO 6 SECONDS, LIVING POSTER: everything holds position. Only micro-life remains:
> the signal accent pulses once at very low amplitude, a connector line shimmers
> faintly along its length, shadows breathe by a hair, grain drifts almost
> imperceptibly. Nothing changes location, nothing scales, nothing rotates, nothing
> enters or exits.
>
> AUDIO: no music, no narration, no voices. Only minimal UI-adjacent motion design
> sound: soft whoosh on entrance, a light click on settle, a faint tick on the label.
> All subtle, all low in the mix.
>
> FINAL RULE: the finished clip must feel like a broadcast-grade editorial graphic
> assembling itself with intent, then holding as a still poster, matching the provided
> image exactly from 4 seconds to the end.

### Por que 6 segundos e não 10

Beat de 2 a 3 segundos de narração. Clipe de 6 segundos dá margem de sobra para o
editor cortar onde quiser sem ficar sem cauda. Clipe de 10 segundos por beat é
desperdício de crédito de geração, e é a maior linha de custo do processo inteiro.

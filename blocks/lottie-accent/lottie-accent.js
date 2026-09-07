/**
 * Lottie accent — stamps a power point. Never the LCP.
 * Authoring: cell 1 = JSON link; cell 2 = optional law number / caption.
 */

let playerPromise;

function loadPlayer() {
  if (!playerPromise) {
    playerPromise = import(`${window.hlx.codeBasePath}/scripts/vendor/lottie-web.esm.js`)
      .then((mod) => mod.default);
  }
  return playerPromise;
}

function prefersReducedMotion() {
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

export default async function decorate(block) {
  const rows = [...block.children];
  const first = rows[0];
  const cells = first ? [...first.children] : [];
  const link = block.querySelector('a[href$=".json"]') || block.querySelector('a');
  const captionCell = cells[1] || cells[0];
  const captionText = captionCell
    ? captionCell.textContent.replace(link?.textContent || '', '').trim()
    : '';

  const wrap = document.createElement('div');
  wrap.className = 'la-stage';

  const canvas = document.createElement('div');
  canvas.className = 'la-canvas';
  canvas.setAttribute('aria-hidden', 'true');

  wrap.append(canvas);

  if (captionText) {
    const cap = document.createElement('p');
    cap.className = 'la-caption';
    cap.textContent = captionText;
    wrap.append(cap);
  }

  block.replaceChildren(wrap);

  if (!link) return;

  const src = link.href;
  try {
    const lottie = await loadPlayer();
    const anim = lottie.loadAnimation({
      container: canvas,
      renderer: 'svg',
      loop: !block.classList.contains('once'),
      autoplay: false,
      path: src,
    });

    if (prefersReducedMotion()) {
      anim.goToAndStop(anim.totalFrames ? anim.totalFrames - 1 : 0, true);
      return;
    }

    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) anim.play();
        else anim.pause();
      });
    }, { threshold: 0.35 });
    io.observe(block);
  } catch {
    canvas.classList.add('la-fallback');
  }
}

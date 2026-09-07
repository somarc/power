/**
 * Power point — the one sentence that gets the stamp.
 * Authoring: optional eyebrow cell + the sentence.
 */

export default function decorate(block) {
  const cells = [...block.querySelectorAll(':scope > div > div')];
  const inner = document.createElement('blockquote');
  inner.className = 'pp-quote';

  if (cells.length >= 2) {
    const eye = document.createElement('p');
    eye.className = 'pp-eye';
    eye.textContent = cells[0].textContent.trim();
    inner.append(eye);
    const p = document.createElement('p');
    p.className = 'pp-line';
    p.append(...cells[1].childNodes);
    inner.append(p);
  } else if (cells[0]) {
    const p = document.createElement('p');
    p.className = 'pp-line';
    p.append(...cells[0].childNodes);
    inner.append(p);
  }

  block.replaceChildren(inner);
}

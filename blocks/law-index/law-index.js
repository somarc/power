/**
 * Law index — a court roll, not a card grid.
 * Authoring rows: number | title (linked) | one sentence
 */

export default function decorate(block) {
  const list = document.createElement('ol');
  list.className = 'li-roll';

  [...block.children].forEach((row) => {
    const cells = [...row.children];
    if (!cells.length) return;
    const item = document.createElement('li');
    item.className = 'li-row';

    const num = document.createElement('span');
    num.className = 'li-num';
    num.textContent = (cells[0]?.textContent || '').trim().padStart(2, '0');

    const body = document.createElement('div');
    body.className = 'li-body';
    const titleCell = cells[1] || cells[0];
    const link = titleCell.querySelector('a');
    const title = document.createElement(link ? 'a' : 'p');
    title.className = 'li-title';
    if (link) {
      title.href = link.href;
      title.textContent = link.textContent.trim();
    } else {
      title.textContent = titleCell.textContent.trim();
    }
    body.append(title);

    if (cells[2]) {
      const lede = document.createElement('p');
      lede.className = 'li-lede';
      lede.textContent = cells[2].textContent.trim();
      body.append(lede);
    }

    item.append(num, body);
    list.append(item);
  });

  block.replaceChildren(list);
}

const expandCard = require('./expandCard');

test('expands card with id 1 and returns true', () => {
  expect(expandCard(1)).toBe(true);
});
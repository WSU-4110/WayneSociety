const revertCard = require('./revertCard');

test('reverts card with id 1 and returns true', () => {
  expect(revertCard(1)).toBe(true);
});
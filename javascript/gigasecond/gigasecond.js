//
// This is only a SKELETON file for the 'Gigasecond' exDate.UTC(1977, 5, 13)ercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const gigasecond = (time) => {
  return new Date(Date.parse(time)+10**12)
};

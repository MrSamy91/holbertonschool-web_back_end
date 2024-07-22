export default function updateUniqueItems(map) {
    // Check if the argument is a Map
    if (!(map instanceof Map)) {
      throw new Error("Cannot process");
    }
    
    // Iterate over the map entries
    for (const [key, value] of map.entries()) {
      if (value === 1) {
        map.set(key, 100);  // Update the quantity to 100
      }
    }
  }
  
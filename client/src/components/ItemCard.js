function ItemCard() {
  const {name, image, price, reviews, category} = item


  return (
    <div>
      <h2>{category}</h2>
      <h1>{name}</h1>
      <img src={image} alt={name}/>
      <h2>{price}</h2>
      {reviews.map(rev => <h3>{rev}</h3>)}
    </div>
  )
}

export default ItemCard
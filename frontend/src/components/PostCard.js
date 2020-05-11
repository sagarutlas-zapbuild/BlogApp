import React from 'react'
import Card from 'react-bootstrap/Card'
import { Link } from 'react-router-dom'
const PostCard = (props) => {
  console.log(props);

  return (<Card>
    <Card.Header> <Card.Link as={Link} to={"/post/" + props.id}>{props.title}</Card.Link></Card.Header>
    <Card.Body>
      <blockquote className="blockquote mb-0">
        <p>
          {' '}
          {props.summary}{' '}
        </p>
        <footer className="blockquote-footer">
          {props.intro}
          <Link to="/author"><cite title="Source Title">{props.author}</cite></Link>
        </footer>
      </blockquote>
    </Card.Body>
  </Card>)
}

export default PostCard
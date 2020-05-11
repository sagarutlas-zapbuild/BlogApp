import React, { Component } from 'react'
import Container from 'react-bootstrap/Container'
import PostCard from './PostCard'
import { posts } from './constants/urls'

class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
            allPosts: []
        };
    }



    componentDidMount() {
        fetch(posts)
            .then(res => {
                return res.json();
            })
            .then((data) => {
                this.setState({ allPosts: data });
            }).catch((error) => console.log(error));
    }

    render() {
        return (<Container>
            {this.state.allPosts.map(post => {
                console.log(post)
                return (<PostCard author={post.author} title={post.title} summary={post.summary} key={post.id} id={post.id} />)
            })

            }
        </Container>);
    }
}



export default Home
import React, { Component } from 'react'
import { posts } from './constants/urls';
import { Link } from 'react-router-dom';
import { rawPost } from './constants/rawdata'

class Post extends Component {
    constructor(props) {
        super(props);
        this.state = {
            content: "",
            author: "",
            published_at: "",
            parent: "",
            parent_title: "",
            parent_id: "",
            id: props.match.params.id,
        }
        this.previousPost = this.previousPost.bind(this);
    }

    previousPost() {
        this.setState(rawPost);
        fetch(posts + this.state.parent_id + "/")
            .then(res => {
                return res.json();
            })
            .then((data) => {
                this.setState(data);
            }).catch((error) => console.log(error));
    }

    componentDidMount() {
        fetch(posts + this.state.id + "/")
            .then(res => {
                return res.json();
            })
            .then((data) => {
                this.setState(data);
            }).catch((error) => console.log(error));
    }


    render() {
        return (<>
            <h1>{this.state.title}</h1>
            <hr />
            <p>
                {this.state.content}
            </p>
            <hr />
            <label>
                Previous Post in Series: <Link to={"/post/" + this.state.parent_id} onClick={() => this.previousPost()}>{this.state.parent_title}</Link>
            </label>
        </>);
    }
}

export default Post
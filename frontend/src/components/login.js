import React from 'react'

export const login = ()=>{

    return(<div>
        <form className="APP">
            <label htmlFor="username">Email</label>
            <input type="email" name="username"></input>
            <br/>
            <label htmlFor="password">Email</label>
            <input type="password" name="password"></input>
            <br/>
            <input type="submit" title="Login"></input>
            
        </form>
    </div>)
}
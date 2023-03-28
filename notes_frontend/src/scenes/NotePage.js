import React, { useState, useEffect } from 'react';
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'

const NotePage = ({ match, history }) => {

    let noteId = match.params.id;
    let [ note, setNote ] = useState(null);

    useEffect(() => {
        getNote()
    }, [noteId]);

    let getNote = async () => {
        let response = await fetch(`/api/notes/${noteId}`);
        let data = await response.json();
        setNote(data);
    };

    let updateNote = async () => {
        fetch(`http://localhost:8000/api/notes/${noteId}/update/`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(note)
            });
    };

    let deleteNote = async () => {
        fetch(`http://localhost:8000/api/notes/${noteId}/delete/`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            }
        });
        history.push("/")
    }

    let handleSubmit = () => {
        updateNote();
        history.push("/")
    };

    return (
        <div className="note">
            <div className="note-header">
                <h3>
                    <ArrowLeft onClick={handleSubmit} />
                </h3>
                <button onClick={deleteNote}>Delete</button>
            </div>
            <textarea onChange={(e) => { setNote({...note, 'body':e.target.value })}} defaultValue={note?.body}></textarea>
        </div>
    );
};

export default NotePage;
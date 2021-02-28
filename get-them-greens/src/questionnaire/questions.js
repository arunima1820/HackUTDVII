import React, { useState } from "react"
import {
    Button,
    Typography,
    Stepper,
    Step,
    StepLabel,
    TextField,
    FormGroup
} from "@material-ui/core"

export default function Questionnaire(props) {
    const {setUserData} = props

    return (
        <>
            <FormGroup>
                <TextField label="Enter ZIP Code" onChange={setUserData} />
            </FormGroup>
        </>
    )
}
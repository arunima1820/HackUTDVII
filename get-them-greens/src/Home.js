import React, { useState } from "react";
import logo from './temochome.gif';
import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle
} from "@material-ui/core";
import Questionnaire from './questionnaire/questions'

export default function Home() {
    const [open, setOpen] = useState(false);
    const [userData, setUserData] = useState();

    const handleBtnClick = () => {
        setOpen(true);
    }

    const handleClose = () => {
        setOpen(false);
    }

    const storeCollectedData = (input) => {
        setUserData(input);
    }

    return (
        <>
            <img src={logo} height="500rem" />
            <div>
                <Dialog open={open} onClose={handleClose}>
                    <DialogTitle>Tell us what you want</DialogTitle>
                    <DialogContent>
                        <Questionnaire setUserData={storeCollectedData} />
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={handleClose} color="primary">
                            Save
                        </Button>
                    </DialogActions>
                </Dialog>
            </div>
        </>
    )

}
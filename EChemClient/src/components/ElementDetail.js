import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';

function ElementDetail() {
  const { element } = useParams();

  useEffect(() => {
  const urlParams = new URLSearchParams(window.location.search);
    const elementSymbol = urlParams.get('element');
    document.getElementById('elementSymbol').innerText = elementSymbol;  }, []);

  return (
    <div>
      <h1>Element Detailseite</h1>
      <p>Du hast das Element mit dem Symbol <strong>{element}</strong> ausgewählt.</p>
    </div>
  );
}

export default ElementDetail;

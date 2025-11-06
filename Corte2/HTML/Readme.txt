<<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Comparación: Ninja H2R vs BMW M1000RR vs Ducati Superleggera</title>
  <style>
    :root{
      --bg:#f6f7fb; --ink:#1b1f23; --muted:#667085; --brand:#0a84ff; --panel:#ffffff; --accent:#16a34a;
    }
    *{box-sizing:border-box}
    body{margin:0; font-family:Arial, Helvetica, sans-serif; background:var(--bg); color:var(--ink); line-height:1.5}
    header{background:#111827; color:#fff; padding:24px 16px; text-align:center}
    header a{color:#9bd1ff; font-weight:700; text-decoration:none}
    header a:hover{text-decoration:underline}
    main{max-width:1100px; margin:24px auto; padding:0 16px}
    .lead{background:var(--panel); border-radius:12px; padding:18px; box-shadow:0 8px 24px rgba(0,0,0,.06)}
    .gallery{display:grid; gap:16px; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); margin:22px 0}
    .card{background:var(--panel); border-radius:14px; overflow:hidden; box-shadow:0 8px 24px rgba(0,0,0,.06)}
    .card img{width:100%; height:220px; object-fit:cover; display:block}
    .card h3{margin:12px 14px 8px}
    .card p{margin:0 14px 14px; color:var(--muted)}
    table{width:100%; border-collapse:collapse; background:var(--panel); border-radius:12px; overflow:hidden; box-shadow:0 8px 24px rgba(0,0,0,.06)}
    th,td{padding:12px 10px; border-bottom:1px solid #e6e8ef; text-align:center}
    th{background:#111827; color:#fff}
    tr:nth-child(even) td{background:#f2f4f8}
    .note{font-size:0.9rem; color:var(--muted); margin-top:8px}
    footer{margin:28px 0 18px; text-align:center; color:var(--muted)}
    .pill{display:inline-block; padding:2px 8px; border-radius:999px; background:#eef6ff; color:#084cba; font-weight:700; font-size:0.85rem}
    .u{ text-decoration: underline; }
    .red{ color:#dc2626; }
    .green{ color:var(--accent); }
    .blue{ color:#2563eb; }
  </style>
</head>
<body>

  <header>
    <h1>Comparación de Superbikes</h1>
    <h3>Juan David Alonso - 20241005062</h3>
    <h2 class="pill">Ninja H2R · BMW M 1000 RR · Ducati Superleggera</h2>
    <p>
      Repositorio del proyecto: 
      <a href="https://github.com/JuanAlonsoC/proyectosProgramacionAplicada/tree/main/Corte2/HTML" target="_blank" rel="noopener">
        github.com/JuanAlonsoC/proyectosProgramacionAplicada/tree/main/Corte2/HTML
      </a>
    </p>
  </header>

  <main>
    <section class="lead">
      <h2>¿De qué trata esta página?</h2>
      <p>
        Esta página web presenta una <strong>comparación</strong> entre tres motos <em>hiperdeportivas</em>: la <strong>Kawasaki Ninja H2R</strong>, la <strong>BMW M 1000 RR</strong> y la <strong class="u">Ducati Superleggera</strong>.
      </p>
    </section>

    <h2>Galería</h2>
    <div class="gallery">
      <article class="card">
        <img src="H2R.jpg" alt="Kawasaki Ninja H2R"/>
        <h3>Kawasaki Ninja H2R</h3>
        <p>Supercargada, <b class="green">potencia extrema</b> de pista.</p>
        <p><a href="https://www.kawasaki.com" target="_blank" rel="noopener">Sitio oficial</a></p>
      </article>

      <article class="card">
        <img src="BMW.webp" alt="BMW M 1000 RR"/>
        <h3>BMW M 1000 RR</h3>
        <p>Paquete aerodinámico M, electrónica avanzada.</p>
        <p><a href="https://www.bmw-motorrad.com" target="_blank" rel="noopener">Sitio oficial</a></p>
      </article>

      <article class="card">
        <img src="DUCATI.jpg" alt="Ducati Superleggera"/>
        <h3>Ducati Superleggera</h3>
        <p>Chasis de <span class="u">fibra de carbono</span>, ligereza <i class="red">extrema</i>.</p>
        <p><a href="https://www.ducati.com" target="_blank" rel="noopener">Sitio oficial</a></p>
      </article>
    </div>

    <h2>Tabla comparativa (valores de referencia)</h2>
    <table>
      <tr>
        <th>Modelo</th>
        <th>Motor</th>
        <th>Potencia aprox.</th>
        <th>Peso aprox.</th>
        <th>Enfoque</th>
      </tr>
      <tr>
        <td><b>Kawasaki Ninja H2R</b></td>
        <td>998cc, 4L, <u>supercargado</u></td>
        <td class="green"><b>>300 hp</b></td>
        <td>~216 kg</td>
        <td><span class="red"><i>Pista</i></span></td>
      </tr>
      <tr>
        <td><b>BMW M 1000 RR</b></td>
        <td>999cc, 4L</td>
        <td>~212 hp</td>
        <td>~192 kg</td>
        <td>Superbike homologada</td>
      </tr>
      <tr>
        <td><b>Ducati Superleggera</b></td>
        <td>998cc, V4</td>
        <td>~224 hp</td>
        <td class="blue"><b>~159 kg (seca)</b></td>
        <td>Ligereza y agilidad</td>
      </tr>
    </table>
    <p class="note">* Cifras orientativas; pueden variar por año y configuración.</p>

    <h2>Enlaces rápidos</h2>
    <ul>
      <li><a href="https://github.com/JuanAlonsoC/proyectosProgramacionAplicada/tree/main/Corte2/HTML" target="_blank">Carpeta del proyecto en GitHub</a></li>
      
    </ul>
  </main>

  <footer>
    © 2025 · Página de comparación de superbikes (ZAUZIZEZO).
  </footer>
</body>
</html>


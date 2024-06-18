using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            estudiante est = new estudiante();
            est.Nombre=(textBox1.Text);
            est.Apellido=(textBox2.Text);
            est.Escuela=(textBox3.Text);
            Estudiante con = new Estudiante();
            con.Guardar(est);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            dataGridView1.Columns.Add("NombreColumna", "Nombre");
            dataGridView1.Columns.Add("ApellidoColumna", "Apellido");
            dataGridView1.Columns.Add("EscuelaColumna", "Escuela");
            Estudiante con = new Estudiante();
            List<estudiante> lista = con.ObtenerEstudiantes();
            dataGridView1.Rows.Clear();
            foreach (estudiante est in lista)
            {
                dataGridView1.Rows.Add(est.Nombre, est.Apellido, est.Escuela);
            }

            
        }
    }
}

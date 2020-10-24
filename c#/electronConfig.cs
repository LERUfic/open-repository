using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ElectronConfig
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] num = { 2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6 };           
            string[] spdf2 = { "1s", " 2s", " 2p", " 3s", " 3p", " 4s", " 3d", " 4p", " 5s", " 4d", " 5p", " 6s", " 3f", " 5d", " 6p", " 7s", " 5f", " 6d", " 7p" };

            int soma = 0;
            string config = "";

            Console.WriteLine("Atomic number");
            
            int z = int.Parse(Console.ReadLine());
            int currentZ = z;

            for (int i = 0; z > 0; i++){
                z -= num[i];
                if (z < 0){
                    num[i] = currentZ - soma;
                    config += (spdf2[i] + num[i]);
                    break;
                }
                config += spdf2[i] + num[i];
                soma += num[i];
            }
            Console.WriteLine(config);
        }
    }
}
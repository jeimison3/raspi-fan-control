## Ciração do serviço
```shell
sudo nano /etc/systemd/system/fan.service
```
(Modifique nas linhas `WorkingDirectory` e `ExecStart` o diretório do repositório)

```
[Unit]
Description=Fan service startup
After=network.target
StartLimitIntervalSec=0

[Service]
Type=exec
WorkingDirectory=/opt/fan
ExecStart=/opt/fan/.venv/bin/python3 fan.py
RemainAfterExit=true

[Install]
WantedBy=multi-user.target
```
```shell
sudo systemctl enable fan.service
sudo systemctl start fan.service
```
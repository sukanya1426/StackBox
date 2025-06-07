FROM node:20-alpine 
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

EXPOSE 3000

# Change this line to use Next.js's built-in server instead of serve
CMD ["npm", "start"]
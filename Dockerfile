# Step 1: Use official Node.js image
FROM node:18-alpine

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Step 4: Copy rest of the app
COPY . .

# Step 5: Build the React app
RUN npm run build

# Step 6: Use Nginx to serve the build
FROM nginx:alpine
COPY --from=0 /app/build /usr/share/nginx/html

# Optional: Expose port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

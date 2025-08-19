FROM node:lts

WORKDIR /myapp

# Copy source code and dependencies
COPY package*.json ./

# Install dependencies
RUN npm install


COPY . .

# Expose the app port (adjust if your app uses a different one)
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
